import json
import logging

from .models import User
from apps.user import forms
from utils import result, regular, md5, jwts


# 用户登录
def login(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
    except Exception as e:
        logging.info("错误信息：{}", format(e))
        return R.failed("参数错误")
    # 表单验证
    form = forms.UserLoginForm(dict_data)
    if not form.is_valid():
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)
    # 登录
    user_name = form.cleaned_data.get('userName')
    password = form.cleaned_data.get('password')
    user_resp = User.objects.filter(user_name=user_name, status=1, delete_flag=0).first()
    if not user_resp:
        return R.failed(msg="用户名或密码错误")
    encrypt_pwd = md5.getPassword(password)
    if encrypt_pwd != user_resp.password:
        return R.failed(msg="用户名或密码错误")
    payload = {"userName": user_resp.user_name, "id": user_resp.id, "email": user_resp.email, "phone": user_resp.phone}
    key = jwts.create_token(payload)
    user_resp.password = None
    result = {"Authorization": key, "userInfo": payload}
    # 返回结果
    return R.ok(data=result)


# 用户注册
def register(request):
    try:
        # 接收请求参数
        json_data = request.body.decode()
        # 参数为空判断
        if not json_data:
            return R.failed("参数不能为空")
        # 数据类型转换
        dict_data = json.loads(json_data)
    except Exception as e:
        logging.info("错误信息：{}", format(e))
        return R.failed("参数错误")
    # 表单验证
    form = forms.UserRegisterForm(dict_data)
    if not form.is_valid():
        # 获取错误信息
        err_msg = regular.get_err(form)
        # 返回错误信息
        return R.failed(err_msg)
    User.objects.create(
        user_name=form.cleaned_data.get("userName"),
        password=md5.getPassword(form.cleaned_data.get("password")),
        email=form.cleaned_data.get("email"),
        phone=form.cleaned_data.get("phone"),
        status=1,
        delete_flag=0
    )
    return R.ok(data="注册成功")


# 获取当前登录用户
def get_user(request):
    return R.ok(data=request.jwt_user)


# 登出
def logout(request):
    return R.ok()
