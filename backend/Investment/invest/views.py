from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import  UserSerializer,ContactSerializer,InvestSerializer


# A login API 
@api_view(['POST'])
def login(request):
    user=get_object_or_404(User,username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"details":"Info Not Found"})
    token,created=Token.objects.get_or_create(user=user)
    serializer=UserSerializer(instance=user)
    return Response({"token":token.key,"user":serializer.data})
  

# A register API
@api_view(['POST'])
def register(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user=User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token=Token.objects.create(user=user)
        return Response({"token":token.key,"user":serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# An API to add a contact information 
@api_view(["POST"])
def contact(request):
    serializer=ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Response": "Message Sent Successfully"})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# An API to add investment 
@api_view(["POST"])
def invest(request):
    serializer=InvestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({{"Response": "Investment request successfully sent"}})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)