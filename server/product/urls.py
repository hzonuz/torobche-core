
from django.urls import path

from product.views import ProductDetailView, ProductListView, RedirectToProductView

app_name = 'prodcut'
urlpatterns = [
    path('v0/', ProductListView.as_view(), name='products-v0'),
    path('<product_id>/v0/', ProductDetailView.as_view(), name='product-detail-v0'),
    path('<product_id>/redirect/v0/', RedirectToProductView.as_view(), name='redirect-to-product-v0'),
]