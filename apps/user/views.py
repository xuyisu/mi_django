
from django.utils.decorators import method_decorator
from django.views import View

from apps.user import services
from middleware.login_middleware import check_login

from utils import result


# 查询用户分页数据
@method_decorator(check_login, name="post")
class LoginView(View):

    # 接收POST请求
    def post(self, request):
        # 调用查询用户分页数据方法
        result = services.login(request)
        # 返回结果
        return result


# 查询用户详情
@method_decorator(check_login, name="post")
class RegisterView(View):
    def post(self, request):
        # 调用查询用户详情服务方法
        result = services.register(request)
        # 返回结果
        return result


# 添加用户
@method_decorator(check_login, name="get")
class GetUserView(View):

    def get(self, request):
        # 获取当前用户信息
        result = services.get_user(request)
        # 返回结果
        return result


# 更新用户
@method_decorator(check_login, name="post")
class LogoutView(View):
    # 接收PUT请求
    def post(self, request):
        # 登出
        result = services.logout(request)
        # 返回结果
        return result