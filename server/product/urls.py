
from django.urls import path

from product.views import ProductListView

app_name = 'prodcut'
urlpatterns = [
    path('v0/', ProductListView.as_view(), name='products-v0'),
]