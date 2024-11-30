from datetime import datetime

from . import forms
from .models import UserAddress
from django.core.paginator import Paginator
from constants.constants import PAGE_LIMIT, USER_ID
from utils import result, regular, snowflake
import json
import logging


# 分页查询地址信息
def page_list(request):
    user_id = request.jwt_user.id
    # 页码
    page = int(request.GET.get("current", 1))
    # 每页数
    limit = int(request.GET.get("size", PAGE_LIMIT))
    # 实例化查询对象
    query = UserAddress.objects.filter(create_user=user_id, delete_flag=False)
    # 排序
    query = query.order_by("id")
    # 设置分页
    paginator = Paginator(query, limit)
    # 记录总数
    count = paginator.count
    # 分页查询
    # 分页查询
    user_list = paginator.page(page)
    # 实例化结果
    records = []
    # 遍历数据源
    if len(user_list) > 0:
        for item in user_list:
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


# 添加地址
def add_address(request):
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
    form = forms.UserAddressForm(dict_data)
    if form.is_valid():
        # 创建用户地址
        UserAddress.objects.create(
            receive_name=form.cleaned_data.get('receiveName'),
            receive_phone=form.cleaned_data.get('receivePhone'),
            province=form.cleaned_data.get('province'),
            province_code=form.cleaned_data.get('provinceCode'),
            city=form.cleaned_data.get('city'),
            city_code=form.cleaned_data.get('cityCode'),
            area=form.cleaned_data.get('area'),
            area_code=form.cleaned_data.get('areaCode'),
            street=form.cleaned_data.get('street'),
            default_flag=form.cleaned_data.get('defaultFlag'),
            postal_code=form.cleaned_data.get('postalCode'),
            address_label=form.cleaned_data.get('addressLabel'),
            create_user=user_id,
            update_user=user_id,
            delete_flag=0,
            address_id=snowflake.generate_id()
        )
        # 返回结果
        return R.ok(msg="创建成功")
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)


# 地址详情
def get_address_detail(address_id):
    user_address_resp = UserAddress.objects.filter(delete_flag=0, address_id=address_id).first()
    if not user_address_resp:
        return R.failed(msg="当前地址不存在，请重新添加")
    return R.ok(data=UserAddress.to_dict(user_address_resp))


# 用户地址删除
def delete_address(address_id, request):
    user_id = request.jwt_user.id
    user_address_resp = UserAddress.objects.filter(delete_flag=0, address_id=address_id).first()
    if not user_address_resp:
        return R.failed(msg="当前地址不存在，请重新添加")
    user_address_resp.delete_flag = 1
    user_address_resp.update_user = user_id
    user_address_resp.save()
    return R.ok()


# 更新地址
def update_address(request, address_id):
    user_address_resp = UserAddress.objects.filter(delete_flag=0, address_id=address_id).first()
    if not user_address_resp:
        return R.failed(msg="当前地址不存在，请重新添加")
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
    user_id = request.jwt_user.id
    # 表单验证
    form = forms.UserAddressForm(dict_data)
    if form.is_valid():
        # 创建用户地址
        user_address_resp.receive_name = form.cleaned_data.get('receiveName')
        user_address_resp.receive_phone = form.cleaned_data.get('receivePhone')
        user_address_resp.province = form.cleaned_data.get('province')
        user_address_resp.province_code = form.cleaned_data.get('provinceCode')
        user_address_resp.city = form.cleaned_data.get('city')
        user_address_resp.city_code = form.cleaned_data.get('cityCode')
        user_address_resp.area = form.cleaned_data.get('area')
        user_address_resp.area_code = form.cleaned_data.get('areaCode')
        user_address_resp.street = form.cleaned_data.get('street')
        user_address_resp.default_flag = form.cleaned_data.get('defaultFlag')
        user_address_resp.postal_code = form.cleaned_data.get('postalCode')
        user_address_resp.address_label = form.cleaned_data.get('addressLabel')
        user_address_resp.update_user = user_id
        user_address_resp.update_time = datetime.now()
        # 更新
        user_address_resp.save()
        # 返回结果
        return R.ok(msg="更新成功")
    else:
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)
