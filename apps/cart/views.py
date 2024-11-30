from django.utils.decorators import method_decorator
from django.views import View

from apps.cart import services
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired


@method_decorator(check_login, name="get")
class CartListView(PermissionRequired, View):
    # 接收GET请求
    def get(self, request):
        # 调用查询商品分页数据方法
        result = services.page_list(request)
        # 返回结果
        return result


# 添加到购物车
@method_decorator(check_login, name="post")
class CartAddView(PermissionRequired, View):
    # 接收Post请求
    def post(self, request):
        # 调用查询商品分页数据方法
        result = services.add_cart(request)
        # 返回结果
        return result


@method_decorator(check_login, name="put")
class CartDetailView(PermissionRequired, View):
    # 接收Post请求
    # 改变数量
    def put(self, request, product_id):
        # 调用查询商品分页数据方法
        result = services.update_cart(request, product_id)
        # 返回结果
        return result

    # 删除购物车商品
    def delete(self, request, product_id):
        # 调用查询商品分页数据方法
        result = services.delete_cart(product_id, request)
        # 返回结果
        return result


@method_decorator(check_login, name="put")
class CartSelectAllView(PermissionRequired, View):
    # 接收Post请求
    def put(self, request):
        # 调用查询商品分页数据方法
        result = services.select_all(request)
        # 返回结果
        return result


@method_decorator(check_login, name="put")
class CartUnSelectAllView(PermissionRequired, View):
    # 接收Post请求
    def put(self, request):
        # 调用查询商品分页数据方法
        result = services.un_select_all(request)
        # 返回结果
        return result


@method_decorator(check_login, name="get")
class CartSumView(PermissionRequired, View):
    # 接收Post请求
    def get(self, request):
        # 调用查询商品分页数据方法
        result = services.sum_cart(request)
        # 返回结果
        return result
