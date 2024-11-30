import json
import logging

from django.db import transaction

from . import forms
from .models import Cart
from django.core.paginator import Paginator
from constants.constants import PAGE_LIMIT, USER_ID
from utils import result
from ..activity.models import Activity
from ..product.models import Product
from datetime import datetime


# 订单列表
def page_list(request):
    user_id = request.jwt_user.id
    # 页码
    page = int(request.GET.get("current", 1))
    # 每页数
    limit = int(request.GET.get("size", PAGE_LIMIT))
    # 实例化查询对象
    query = Cart.objects.filter(user_id=user_id, delete_flag=False)
    # 排序
    query = query.order_by("id")
    # 设置分页
    paginator = Paginator(query, limit)
    # 记录总数
    count = paginator.count
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
    result = {
        "total": count,
        "records": records,
        "current": page,
        "size": limit,
    }
    # 返回结果
    return R.ok(data=result)


# 添加购物车
@transaction.atomic
def add_cart(request):
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
    form = forms.CartAddForm(dict_data)
    if form.is_valid():
        # 获取数据
        product_id = form.cleaned_data.get("productId")
        # TODO 更换枚举
        product = Product.objects.filter(product_id=product_id, status=1).first()
        if not product:
            return R.failed("当前商品已下架或删除")
        # 查询当前商品是否已存在购物车
        cart_exist = Cart.objects.filter(delete_flag=False, user_id=user_id, product_id=product_id).first()
        if not cart_exist:
            cart_create = Cart()
            cart_create.product_id = product_id
            cart_create.activity_id = product.activity_id
            cart_create.create_user = user_id
            cart_create.user_id = user_id
            cart_create.product_subtitle = product.sub_title
            cart_create.product_unit_price = product.price
            cart_create.product_main_image = product.main_image
            cart_create.product_name = product.name
            cart_create.quantity = 1
            cart_create.product_total_price = cart_create.product_unit_price * cart_create.quantity
            activity = Activity.objects.filter(activity_id=product.activity_id).first()
            if activity:
                cart_create.activity_name = activity.name
            cart_create.save()
        else:
            cart_exist.update_time = None
            cart_exist.update_user = user_id
            cart_exist.quantity = cart_exist.quantity + 1
            cart_exist.product_total_price = cart_exist.product_unit_price * cart_exist.quantity
            cart_exist.save()
    return sum_cart(request)


# 改变购物车数量
@transaction.atomic
def update_cart(request, product_id):
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
    # TODO 更换枚举
    product = Product.objects.filter(product_id=product_id, status=1).first()
    if not product:
        return R.failed("当前商品已下架或删除")
    cart_exist = Cart.objects.filter(delete_flag=False, user_id=user_id, product_id=product_id).first()
    if not cart_exist:
        return R.failed("购物车已不存在该商品")
    type = dict_data["type"]
    # selected = dict_data["selected"]
    cart_exist.update_time = None
    if 1 == type:
        cart_exist.quantity = cart_exist.quantity + 1
    else:
        if cart_exist.quantity <= 1:
            return R.failed("购物车商品数量不足")
        else:
            cart_exist.quantity = cart_exist.quantity - 1
    cart_exist.product_total_price = cart_exist.product_unit_price * cart_exist.quantity
    cart_exist.update_user = user_id
    cart_exist.save()
    return R.ok()


# 删除购物车商品
@transaction.atomic
def delete_cart(product_id, request):
    user_id = request.jwt_user.id
    cart_list = Cart.objects.filter(delete_flag=False, user_id=user_id, product_id=product_id).all()
    if len(cart_list) > 0:
        for item in cart_list:
            # 对象
            item.delete_flag = True
            item.update_user = user_id
            item.update_time = datetime.now()
            # 加入数组
            item.save()
    return R.ok()


# 全选
@transaction.atomic
def select_all(request):
    user_id = request.jwt_user.id
    cart_list = Cart.objects.filter(delete_flag=False, user_id=user_id, selected=False).all()
    if len(cart_list) > 0:
        for item in cart_list:
            # 对象
            item.is_select = True
            item.update_user = user_id
            item.update_time = datetime.now()
            # 加入数组
            item.save()
    return R.ok()


# 取消全选
@transaction.atomic
def un_select_all(request):
    user_id = request.jwt_user.id
    cart_list = Cart.objects.filter(delete_flag=False, user_id=user_id, selected=True).all()
    if len(cart_list) > 0:
        for item in cart_list:
            # 对象
            item.is_select = False
            item.update_user = user_id
            item.update_time = datetime.now()
            # 加入数组
            item.save()
    return R.ok()


# 获取购物车数量
def sum_cart(request):
    user_id = request.jwt_user.id
    count = Cart.objects.filter(delete_flag=False, user_id=user_id).count()
    return R.ok(data=count)
