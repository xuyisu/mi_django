from rest_framework import viewsets
from .models import OrderDetail
from .serializers import OrderDetailSerializer
class OrderDetailViewSet(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer