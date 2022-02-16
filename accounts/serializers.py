from rest_framework import serializers
from . models import Account
from django.contrib.auth import authenticate


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'name', 'phone', 'address', 'is_admin')

class SignupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('email', 'password', 'name', 'phone', 'address')
        extra_kwargs = {
            'password':{
                'write_only':True
                }
            }
    
    def create(self, validated_data):
        account = Account.objects.create_user(
            validated_data['email'], 
            validated_data['password'], 
            validated_data['name'],
            validated_data['phone'],
            validated_data['address']
        )
        return account

class LoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        account = authenticate(**attrs)

        if account and account.is_active:
            return account
        else:
            raise serializers.ValidationError("Wrong email/password.")
        