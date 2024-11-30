from django.urls import path  # 导入路径相关配置
from apps.user_address import views

urlpatterns = [
    # 查询用户地址分页列表
    path('pages', views.UserAddressListView.as_view()),
    # 添加用户地址
    path('add', views.UserAddressAddView.as_view()),
    # 查询、删除用户地址详情
    path('<int:address_id>', views.UserAddressDetailView.as_view()),
]
