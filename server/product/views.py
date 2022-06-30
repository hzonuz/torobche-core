from django.http import HttpResponseRedirect
from rest_framework import generics, filters, views

from product.serializers import ProductDetailSerializer, ProductSerializer
from product.models import Product
from product.filters import FilterCategories

class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, FilterCategories]
    search_fields = ['name']
    ordering_fields = ['price', 'created_at']

    def get_queryset(self):
        return Product.objects.all()
    

class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer

    def get_object(self):
        product = self.kwargs.get('product_id')
        return Product.objects.get(id=product)


class RedirectToProductView(views.APIView):
    def get(self, request, *args, **kwargs):
        product = self.kwargs.get('product_id')
        url = Product.objects.get(id=product).url
        return HttpResponseRedirect(url)