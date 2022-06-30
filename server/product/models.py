from django.db import models
from django.contrib.auth.models import User

from shop.models import Shop


class Category(models.Model):
    name = models.CharField(max_length=64)
    subcategory = models.ForeignKey(
        "self", blank=True, related_name="subcat", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="product_category"
    )
    url = models.URLField()
    favourites = models.ManyToManyField(
        User, blank=True, related_name="favourites"
    )
    recents = models.ManyToManyField(
        User, blank=True, related_name="recents"
    )
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name="shop"
    )

    def __str__(self):
        return self.name


class Detail(models.Model):
    category = models.ManyToManyField(Category, related_name="detail_category")
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class DetailValue(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product"
    )
    value = models.CharField(max_length=64)

    def __str__(self):
        return self.value
