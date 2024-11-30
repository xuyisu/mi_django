"""
    返回结果
    code 类型码 200-成功 500-失败
    data 数据
    msg 提示信息
    kwargs 其他参数
"""
from django.http import JsonResponse

from constants.constants import *


def ok(data=None, msg=MESSAGE_OK, code=200, **kwargs):
    message = {"code": code, "data": data, "msg": msg}
    if kwargs:
        message.update(kwargs)
    return JsonResponse(data=message)


def failed(msg=MESSAGE_FAIL, code=500, **kwargs):
    message = {"code": code, "data": None, "msg": msg}
    if kwargs:
        message.update(kwargs)
    return JsonResponse(data=message)
