from rest_framework import generics, exceptions

from shop.serializers import SellerSerializer, ShopSerializer

# Create your views here.
class CreateSellerView(generics.CreateAPIView):
    serializer_class = SellerSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ShopsView(generics.ListCreateAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        if hasattr(self.request.user, 'seller'):
            return self.request.user.seller.shop.all()
        return []

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user.seller)