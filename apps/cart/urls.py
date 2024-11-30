from django.urls import path  # 导入路径相关配置
from apps.cart import views

urlpatterns = [
    # 查询订单分页列表
    path('pages', views.CartListView.as_view()),
    path('add', views.CartAddView.as_view()),
    path('<int:product_id>', views.CartDetailView.as_view()),
    path('selectAll', views.CartSelectAllView.as_view()),
    path('unSelectAll', views.CartUnSelectAllView.as_view()),
    path('sum', views.CartSumView.as_view()),
]
1726995032123