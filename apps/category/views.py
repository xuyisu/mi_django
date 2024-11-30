from django.utils.decorators import method_decorator
from django.views import View

from apps.category import services
from middleware.login_middleware import check_login
from middleware.permission_middleware import PermissionRequired

@method_decorator(check_login, name="get")
class CategoryListView(PermissionRequired, View):
    # 接收GET请求
    def get(self, request):
        # 调用查询用户分页数据方法
        result = services.list()
        # 返回结果
        return result