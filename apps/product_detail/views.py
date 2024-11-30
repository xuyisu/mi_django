from rest_framework import viewsets
from .models import ProductDetail
from .serializers import ProductDetailSerializer
class ProductDetailViewSet(viewsets.ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer