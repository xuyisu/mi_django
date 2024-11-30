from django.utils.decorators import method_decorator
from django.views import View

from apps.order_info import services
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired


@method_decorator(check_login, name="get")
class OrderListView(PermissionRequired, View):
    # 接收GET请求
    def get(self, request):
        # 调用查询商品分页数据方法
        result = services.page_list(request)
        # 返回结果
        return result


# 创建订单
@method_decorator(check_login, name="post")
class OrderCreateView(PermissionRequired, View):

    def post(self, request):
        # 创建订单
        result = services.create_order(request)
        # 返回结果
        return result


# 订单详情
@method_decorator(check_login, name="get")
class OrderDetailView(PermissionRequired, View):
    # 接收GET请求
    def get(self, request, order_no):
        # 调用查询商品分页数据方法
        result = services.order_detail(order_no, request)
        # 返回结果
        return result

    def put(self, request, order_no):
        # 调用查询商品分页数据方法
        result = services.cancel_order(order_no, request)
        # 返回结果
        return result


@method_decorator(check_login, name="post")
class OrderPayView(View):
    def post(self, request):
        # 调用查询商品分页数据方法
        result = services.pay(request)
        # 返回结果
        return result
