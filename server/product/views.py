from rest_framework import generics, filters

from product.serializers import ProductSerializer
from product.models import Product

class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        return Product.objects.all()
    

    