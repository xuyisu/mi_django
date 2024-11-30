from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderStatusRecordViewSet

router = DefaultRouter()
router.register(r'order_status', OrderStatusRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]