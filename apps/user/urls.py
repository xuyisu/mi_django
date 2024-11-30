from django.urls import path  # 导入路径相关配置
from apps.user import views

urlpatterns = [
    # 登录
    path('login', views.LoginView.as_view()),
    # 注册
    path('register', views.RegisterView.as_view()),
    # 查询用户详情
    path('getUser', views.GetUserView.as_view()),
    # 添加用户
    path('logout', views.LogoutView.as_view()),

]
# 用户模块路由
