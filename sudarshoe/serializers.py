from pyexpat import model
from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields=('customer','product','date','trans_status','payment_method','pay_status')