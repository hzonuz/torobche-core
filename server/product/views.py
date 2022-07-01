from django.http import HttpResponseRedirect
from rest_framework import generics, filters, views, response, status

from product.serializers import (
    CategorySerializer,
    DetailSerializer,
    ProductCreateSerializer,
    ProductDetailSerializer,
    ProductSerializer,
)
from product.models import Category, Detail, DetailValue, Product
from product.filters import FilterCategories, FilterPrice
from shop.models import Shop


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, FilterCategories, FilterPrice]
    search_fields = ["name"]
    ordering_fields = ["price", "created_at"]

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer

    def get_object(self):
        product = self.kwargs.get("product_id")
        return Product.objects.get(id=product)


class RedirectToProductView(views.APIView):
    def get(self, request, *args, **kwargs):
        product = self.kwargs.get("product_id")
        url = Product.objects.get(id=product).url
        return HttpResponseRedirect(url)


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class DetailListView(generics.ListAPIView):
    serializer_class = DetailSerializer

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return Detail.objects.filter(
            category__in=Category.objects.filter(id=category_id).get_ancestors(
                include_self=True
            )
        )


class AddProductView(views.APIView):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs.get("product_id")
        product = Product.objects.get(id=product_id)
        shop_id = self.kwargs.get("shop_id")
        shop = Shop.objects.get(id=shop_id)
        product.shop.add(shop)
        return response.Response({"success": True}, status=200)


class CreateProductView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer

    def create(self, request, *args, **kwargs):
        details = request.data.pop("details")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        instance = serializer.instance
        for d in details:
            _id = d.get("id")
            value = d.get("value")
            detail = Detail.objects.get(id=_id)
            DetailValue.objects.create(detail=detail, value=value, product=instance)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
