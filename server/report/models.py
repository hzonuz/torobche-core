from django.db import models

from product.models import Product

# Create your models here.
class Report(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_report"
    )
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="user"
    )
    description = models.TextField()

    def __str__(self):
        return self.description
