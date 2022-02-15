from rest_framework.response import Response
from rest_framework import generics, permissions, status
from . serializers import *
from django.contrib.auth.models import update_last_login

from rest_framework.authtoken.models import Token


class AccountViewsets(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AccountSerializers

    def get_object(self):
        return self.request.user

class SignupViewsets(generics.GenericAPIView):
    serializer_class = SignupSerializers

    def post(self, request, *args, **kwargs):

        #send the data from user to serializer and check the validation
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        #get the account object and update its last login attribute
        account = serializer.save()
        update_last_login(None, account)

        print(Token.objects.get_or_create(user=account))
        print(Token.objects.get_or_create(user=account)[0].key)
        print(Token.objects.get_or_create(user=account)[1])
        
        #create response, account data and token
        return Response({
            #compose account data using accountserializers
            'account':AccountSerializers(account, context=self.get_serializer_context()).data,

            #get the token, its an object with token value inside the 'key' attribute 
            'token':Token.objects.get_or_create(user=account)[0].key            
        })

class LogoutViewsets(generics.GenericAPIView):

    def post(self, request):
        request.user.auth_token.delete()

        return Response(
            {"message":"You're logged out"},
            status=status.HTTP_200_OK
        )