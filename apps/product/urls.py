from django.urls import path  # 导入路径相关配置
from apps.product import views

urlpatterns = [
    # 查询商品分页列表
    path('pages', views.ProductListView.as_view()),
    # 查询商品详情
    path('<int:product_id>', views.ProductDetailView.as_view()),
]
