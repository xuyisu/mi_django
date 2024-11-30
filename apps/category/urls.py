from django.urls import path  # 导入路径相关配置
from apps.category import views

urlpatterns = [
    # 查询用户地址分页列表
    path('list', views.CategoryListView.as_view()),
]
