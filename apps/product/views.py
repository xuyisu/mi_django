from django.utils.decorators import method_decorator
from django.views import View

from apps.product import services
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired


@method_decorator(check_login, name="get")
class ProductListView(PermissionRequired, View):
    # 接收GET请求
    def get(self, request):
        # 调用查询商品分页数据方法
        result = services.page_list(request)
        # 返回结果
        return result

@method_decorator(check_login, name="get")
class ProductDetailView(PermissionRequired, View):
    # 接收GET请求
    def get(self, request, product_id):
        # 调用查询商品详情
        result = services.get_product_detail(product_id)
        # 返回结果
        return result