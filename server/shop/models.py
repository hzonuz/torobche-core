from django.db import models

class Seller(models.Model):
    user = models.OneToOneField(
        "auth.User", on_delete=models.CASCADE, related_name="seller"
    )
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.user.username

class Shop(models.Model):
    name = models.CharField(max_length=64, unique=True)
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, related_name="shop"
    )
    url = models.URLField()

    def __str__(self):
        return self.name

