from urllib import request
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import Product


#For Admin
class ProductViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
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


#For customers, create custom view only allow GET method using decorator from rest_framework
@api_view(['GET'])
def ShoesList(request):
    shoes = Product.objects.all()
    #Get all data to be serialized
    serializer = ProductSerializer(shoes, many=True)
    #return the serialized data
    return Response(serializer.data)