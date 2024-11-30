from django.urls import path  # 导入路径相关配置
from apps.order_info import views

urlpatterns = [
    # 查询订单分页列表
    path('pages', views.OrderListView.as_view()),
    path('create', views.OrderCreateView.as_view()),
    path('pay', views.OrderPayView.as_view()),
    path('<str:order_no>', views.OrderDetailView.as_view()),

]
