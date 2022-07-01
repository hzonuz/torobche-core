
from django.urls import path

from product.views import AddProductView, CategoryListView, CreateProductView, ProductDetailView, ProductListView, RedirectToProductView, DetailListView

app_name = 'prodcut'
urlpatterns = [
    path('v0/', ProductListView.as_view(), name='products-v0'),
    path('create/v0/', CreateProductView.as_view(), name='create-product-v0'),
    path('categories/v0/', CategoryListView.as_view(), name='categories-v0'),
    path('<product_id>/v0/', ProductDetailView.as_view(), name='product-detail-v0'),
    path('<product_id>/redirect/v0/', RedirectToProductView.as_view(), name='redirect-to-product-v0'),
    path('<product_id>/<shop_id>/v0/', AddProductView.as_view(), name='add-product-v0'),
    path('<category_id>/details/v0/', DetailListView.as_view(), name='details-v0'),
]