from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Contact,Wallet,Invest

#  user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ( 'id','username', 'email', 'password')


#  Contact serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta(object):
        model= Contact
        fields="__all__"

#  Wallet serializer
class WalletSerializer(serializers.ModelSerializer):
    class Meta(object):
        model= Wallet
        fields="__all__"

#  Invest serializer
class InvestSerializer(serializers.ModelSerializer):
    class Meta(object):
        model= Invest
        fields="__all__"