from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductDetailViewSet

router = DefaultRouter()
router.register(r'product_detail', ProductDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]