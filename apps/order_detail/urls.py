from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderDetailViewSet

router = DefaultRouter()
router.register(r'order_detail', OrderDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]