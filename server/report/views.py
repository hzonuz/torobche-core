from rest_framework import generics

from report.serializers import ReportSerializer, CreateReportSerializer
from product.models import Product
from report.models import Report

class ReportListView(generics.ListAPIView):
    serializer_class = ReportSerializer
    
    def get_queryset(self):
        if hasattr(self.request.user, 'seller'):
            shops = self.request.user.seller.shop.all()
            products = Product.objects.filter(shop__in=shops)
            return Report.objects.filter(product__in=products)
        return []

class CreateReportView(generics.CreateAPIView):
    serializer_class = CreateReportSerializer

    def perform_create(self, serializer):
        product_id = self.kwargs.get('product_id')
        product = Product.objects.get(id=product_id)
        serializer.save(user=self.request.user, product=product)
