from rest_framework import viewsets, permissions
from .serializers import *
from .models import Product


class ProductViewset(viewsets.ModelViewSet):
    permission_classes = [ permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class TransactionViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TransactionSerializer

    def get_queryset(self):
        #customer is the 'related_name' of FK Account inside the Transaction table
        return self.request.user.customer.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)