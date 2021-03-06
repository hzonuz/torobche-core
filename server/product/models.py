from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

from shop.models import Shop

from mptt.models import MPTTModel, TreeForeignKey
from mptt.managers import TreeManager

class CategoryManager(TreeManager):
    def viewable(self):
        queryset = self.get_queryset().filter(level=0)
        return queryset
class Category(MPTTModel):
    name = models.CharField(max_length=64)
    parent = TreeForeignKey(
        "self", blank=True, null=True, related_name="child", on_delete=models.CASCADE
    )

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return " -> ".join(full_path[::-1])
    
    objects = CategoryManager()


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="product_category"
    )
    url = models.URLField()
    favourites = models.ManyToManyField(User, blank=True, related_name="favourites")
    recents = models.ManyToManyField(User, blank=True, related_name="recents")
    shop = models.ManyToManyField(Shop, related_name="shop")
    created_at = models.DateTimeField(default=datetime.now)

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
        Product, on_delete=models.CASCADE, related_name="detail_value"
    )
    value = models.CharField(max_length=64)

    def __str__(self):
        return self.value
