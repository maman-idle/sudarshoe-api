from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import Product, Transaction



#ApiOverview
@api_view(['GET'])
def ApiOverview(request):
    apiurls = {
        "Admin-only":{
            "Add product":"/api/sudarshoes/product/",
            "Edit product":"/api/sudarshoes/product/<int:product-id>/",
            "Delete product":"/api/sudarshoes/product/<int:product-id>/",
            "Get transaction list":"/api/sudarshoes/transaction-list/",
        },
        "Customers":{
            "Signup":"/api/account/signup/",
            "Login":"/api/account/login/",
            "Logout":"/api/account/logout/",
            "Get current account info":"/api/account/<int:account-id/",
            "Edit current account":"/api/account/<int:account-id/",
            "Create transaction":"/api/sudarshoes/transaction/",
            "Get current account transaction":"/api/sudarshoes/transaction/",
            "Delete current account transaction":"/api/sudarshoes/transaction/<int:trans-id>"
        },
        "Anonymous":{
            "Get product list":"/api/sudarshoes/shoes/"
        }
    }

    return Response(apiurls)


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
    
    #set the attribute 'customer' with the current requesting user
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


#For customers, create custom view only allow GET method using decorator from rest_framework
@api_view(['GET'])
def ShoesList(request):
    shoes = Product.objects.all()
    #Get all data to be serialized
    serializer = ProductSerializer(shoes, many=True)
    #return the serialized data
    return Response(serializer.data)


#Get all transactions for admin
class TransListView(APIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    serializer_class = TransactionSerializer
    
    def get(self, request):
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many=True)
        return Response(serializer.data)
    
    
