import json
import logging
import time
from datetime import datetime
from zoneinfo import ZoneInfo

from django.db import transaction

from . import forms
from .models import OrderInfo
from django.core.paginator import Paginator
from constants.constants import PAGE_LIMIT
from utils import result, regular
from ..activity.models import Activity
from ..cart.models import Cart
from ..order_detail.models import OrderDetail
from ..order_status_record.models import OrderStatusRecord
from ..product.models import Product
from ..user_address.models import UserAddress


# 订单列表
def page_list(request):
    user_id = request.jwt_user.id
    # 页码
    page = int(request.GET.get("current", 1))
    # 每页数
    limit = int(request.GET.get("size", PAGE_LIMIT))
    # 实例化查询对象
    query = OrderInfo.objects.filter(user_id=user_id, delete_flag=False)
    # 排序
    query = query.order_by("id")
    # 设置分页
    paginator = Paginator(query, limit)
    # 记录总数
    count = paginator.count
    # 分页查询
    # 分页查询
    order_list = paginator.page(page)
    # 实例化结果
    records = []
    # 遍历数据源
    if len(order_list) > 0:
        for item in order_list:
            # 对象
            data = item.to_dict()
            # 加入数组
            records.append(data)
    page_result = {
        "total": count,
        "records": records,
        "current": page,
        "size": limit,
    }
    # 返回结果
    return R.ok(data=page_result)


# 创建订单
@transaction.atomic
def create_order(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
    except Exception as e:
        logging.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
        # 表单验证
    form = forms.OrderCreateForm(dict_data)
    if not form.is_valid():
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)
    address_id = form.cleaned_data.get("addressId")
    address = UserAddress.objects.filter(address_id=address_id, delete_flag=False).first()
    user_id = request.jwt_user.id
    if not address:
        return R.failed("当前地址已不存在，请重新添加地址")
    # 从购物车获取商品
    cart_list = Cart.objects.filter(user_id=user_id, selected=True).all()
    if not cart_list:
        return R.failed("恭喜您的购物车已经被清空了，再加一车吧")
    # 生成订单编码
    order_no = str(int(round(time.time() * 1000)))
    total_price = 0
    for cart in cart_list:
        # 查询商品是否售尽
        product = Product.objects.filter(product_id=cart.product_id, delete_flag=False, status=1, stock__gt=0).first()
        if not product:
            return R.failed(f"商品{cart.product_name}已售尽，请选择其它产品")
        # 构建订单明细信息
        order_detail, total_price = save_order_detail(cart, order_no, product, total_price, user_id)
        # 删除购物车信息
        delete_cart(cart)
        # 构建交易记录
        save_order_status_record(order_detail, order_no)

    # 构建订单主表信息
    save_order_info(address, address_id, order_no, total_price, user_id)
    return R.ok(data=order_no)


def delete_cart(cart):
    cart.delete_flag = 1
    cart.save()


def save_order_info(address, address_id, order_no, total_price, user_id):
    order_info = OrderInfo(order_no=order_no,
                           address_id=address_id,
                           province=address.province,
                           city=address.city,
                           area=address.area,
                           street=address.street,
                           postal_code=address.postal_code,
                           receive_name=address.receive_name,
                           payment=total_price,
                           payment_type=1,
                           payment_type_desc="在线支持",
                           receive_phone=address.receive_phone,
                           status=10,
                           status_desc="未付款",
                           create_user=user_id,
                           update_user=user_id,
                           user_id=user_id
                           )
    order_info.save()


def save_order_status_record(order_detail, order_no):
    record = OrderStatusRecord(order_no=order_no,
                               order_detail_no=order_detail.order_detail_no,
                               product_id=order_detail.product_id,
                               product_name=order_detail.product_name,
                               status=order_detail.status,
                               status_desc=order_detail.status_desc)
    record.save()


def save_order_detail(cart, order_no, product, total_price, user_id):
    order_detail = OrderDetail(
        order_no=order_no,
        order_detail_no=str(int(round(time.time()))),
        product_id=cart.product_id,
        product_name=cart.product_name,
        product_main_image=cart.product_main_image,
        quantity=cart.quantity,
        current_unit_price=cart.product_unit_price,
        status=10,
        status_desc="未付款",
        total_price=cart.product_total_price,
        user_id=user_id,
        create_user=user_id
    )
    activity = Activity.objects.filter(activity_id=product.activity_id, delete_flag=False).first()
    if activity:
        order_detail.activity_id = activity.activity_id
        order_detail.activity_name = activity.name
        order_detail.activity_main_image = activity.main_image
    # 总金额
    total_price += cart.product_total_price
    order_detail.save()
    return order_detail, total_price


# 订单详情
def order_detail(order_no, request):
    user_id = request.jwt_user.id
    order_info = OrderInfo.objects.filter(order_no=order_no, delete_flag=False, user_id=user_id).first()
    if order_info:
        order_vo = order_info.to_dict()
        order_detail_list = OrderDetail.objects.filter(order_no=order_no, delete_flag=False).all()
        if len(order_detail_list) > 0:
            for item in order_detail_list:
                order_vo["details"].append(item.to_dict())
        return R.ok(data=order_vo)
    return R.ok()


# 取消订单
@transaction.atomic
def cancel_order(order_no, request):
    user_id = request.jwt_user.id
    order_info = OrderInfo.objects.filter(order_no=order_no, delete_flag=False, user_id=user_id).first()
    if order_info:
        if order_info.status != 10:
            return R.failed(f"当前订单{order_info.status_desc}不允许取消")
        order_info.status = 0
        order_info.status_desc = "已取消"
        order_info.update_user = user_id
        order_info.save()
        order_detail_list = OrderDetail.objects.filter(order_no=order_no, delete_flag=False, user_id=user_id)
        if len(order_detail_list) > 0:
            for item in order_detail_list:
                item.status = 0
                item.status_desc = "已取消"
                item.update_user = user_id
                item.save()
    return R.ok()


# 付款
@transaction.atomic
def pay(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
    except Exception as e:
        logging.info("错误信息：\n{}", format(e))
        return R.failed("参数错误")
        # 表单验证
    user_id = request.jwt_user.id
    form = forms.OrderPayForm(dict_data)
    if not form.is_valid():
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)
    order_no = form.cleaned_data.get("orderNo")
    order_info = OrderInfo.objects.filter(order_no=order_no, delete_flag=False, user_id=user_id, status=10).first()
    if not order_info:
        return R.failed("您没有待支付的订单")
    tz = ZoneInfo('UTC')
    order_info.payment_time = datetime.now(tz)
    order_info.status = 20
    order_info.status_desc = "已付款"
    order_info.save()
    # 订单明细状态更新
    order_detail_list = OrderDetail.objects.filter(order_no=order_no, delete_flag=False, user_id=user_id)
    if len(order_detail_list) > 0:
        for item in order_detail_list:
            item.status = 20
            item.status_desc = "已付款"
            item.save()
            save_order_status_record(item, order_no)

    return R.ok()
