from rest_framework import serializers
from .models import OrderStatusRecord


class OrderStatusRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatusRecord
        fields = '__all__'