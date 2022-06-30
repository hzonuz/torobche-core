from rest_framework import serializers

from product.models import Product
from shop.serializers import ShopSerializer

class ProductSerializer(serializers.ModelSerializer):
    shop  = ShopSerializer()
    class Meta:
        fields = ['id', 'name', 'price', 'description', 'category', 'url', 'shop']
        model = Product