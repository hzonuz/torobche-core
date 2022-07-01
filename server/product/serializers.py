from rest_framework import serializers

from product.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    shop = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        fields = [
            "id",
            "name",
            "price",
            "description",
            "category",
            "url",
            "shop",
            "created_at",
        ]
        model = Product


class ProductDetailSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(read_only=True, slug_field="name")
    shop = serializers.SlugRelatedField(many=True, read_only=True, slug_field="name")

    class Meta:
        fields = [
            "id",
            "name",
            "price",
            "description",
            "category",
            "url",
            "detail",
            "shop",
            "created_at",
        ]
        model = Product

    def get_detail(self, obj):
        res = []
        details = obj.detail_value.all()
        for d in details:
            res.append({d.detail.name: d.value})
        return res

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "id",
            "name",
            "parent",
            "level"
        ]
        model = Category
