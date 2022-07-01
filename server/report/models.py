import enum
from django.db import models

from product.models import Product

class ReportReason(enum.Enum):
    WRONG_PRICE = 1
    WRONG_DESCRIPTION = 2
    WRONG_CATEGORY = 3
    WRONG_URL = 4
    WRONG_SHOP = 5
    WRONG_DETAIL = 6
    OTHER = 7
    UNKNOWN = 8

# Create your models here.
class Report(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_report"
    )
    reason = models.SmallIntegerField(choices=[(i.value, i.name) for i in ReportReason], blank=True, null=True)
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="report"
    )
    description = models.TextField()

    def __str__(self):
        return self.description
