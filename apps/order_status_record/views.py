from rest_framework import viewsets
from .models import OrderStatusRecord
from .serializers import OrderStatusRecordSerializer
class OrderStatusRecordViewSet(viewsets.ModelViewSet):
    queryset = OrderStatusRecord.objects.all()
    serializer_class = OrderStatusRecordSerializer