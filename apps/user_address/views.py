from django.utils.decorators import method_decorator
from django.views import View

from apps.user_address import services
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired


@method_decorator(check_login, name="get")
class UserAddressListView(PermissionRequired, View):
    # 接收GET请求
    def get(self, request):
        # 调用查询用户分页数据方法
        result = services.page_list(request)
        # 返回结果
        return result


@method_decorator(check_login, name="post")
class UserAddressAddView(PermissionRequired, View):
    # 接收GET请求
    def post(self, request):
        # 调用查询用户分页数据方法
        result = services.add_address(request)
        # 返回结果
        return result


# 用户地址详情
@method_decorator(check_login, name="get")
class UserAddressDetailView(PermissionRequired, View):
    # 接收GET请求
    def get(self, request, address_id):
        # 调用查询用户分页数据方法
        result = services.get_address_detail(address_id)
        # 返回结果
        return result

    # 接收DELETE请求
    def delete(self, request, address_id):
        # 调用查询用户分页数据方法
        result = services.delete_address(address_id, request)
        # 返回结果
        return result

    # 接收更新请求
    def put(self, request, address_id):
        # 调用查询用户分页数据方法
        result = services.update_address(request, address_id)
        # 返回结果
        return result
