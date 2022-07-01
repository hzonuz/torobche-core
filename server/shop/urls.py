from django.urls import path

from shop.views import CreateSellerView, ShopsView

app_name = 'shop'
urlpatterns = [
    path('seller/v0/', CreateSellerView.as_view(), name='create_seller'),
    path('v0/', ShopsView.as_view(), name='shops'),
]