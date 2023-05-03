from rest_framework.response import Response
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from rest_framework.authtoken.models import Token
import rest_framework.status as status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt 
import requests
from datetime import datetime
from django.conf import settings
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
@csrf_exempt
@api_view(['POST'])
def loginView(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            token = Token.objects.get(user__username = username)
            user_data = User.objects.get(username=username)
            data = {'name':user_data.get_full_name(),'token':token.key,'id':user_data.id}
            return Response(data=data,status=status.HTTP_200_OK)
        return Response(data='Invalid data')
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET'])
def logoutView(request):
    logout(request)
    return Response(data="Successfully Logout!!")


def loginpage(request):
    return render(request,'login.html')
def Signuppage(request):
    return render(request,'signup.html')

@api_view(['POST'])
def Signupapi(request):
    username = request.data['username']
    email = request.data.get('email')
    password = request.data['password']
    user = User.objects.create_user(username=username,email=email,password=password)
    user.save()
    Token.objects.create(user=user)
    userdata = Token.objects.get(user=user.id)
    api_data = {"token":userdata.key,"username":userdata.user.username}
    data = {
        "data": api_data,
        "status":status.HTTP_201_CREATED
    }
    return Response(data=data,status=status.HTTP_200_OK)
