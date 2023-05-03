from django.shortcuts import render


# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .serializer import *


# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def samples(request):
    if request.method == 'GET':

        obj = Samples.objects.all()
        serializer = SamplesSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = SamplesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        payment_type_id = request.POST.get('payment_type_id',None)
        if payment_type_id is None:
            data = {
                "status":"error",
                "message":"payment_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Samples.objects.get(id=payment_type_id)
        serializer = SamplesSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            data  = {
            "status":"ok",
            "message":"successfull",
            "data":serializer.data
            }
            return Response(data=data,status=status.HTTP_201_CREATED)
        data  = {
            "status":"error",
            "message":serializer.errors,
            }
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        payment_type_id = request.POST.get('payment_type_id',None)
        if payment_type_id is None:
            data = {
                "status":"error",
                "message":"payment_type_id is required"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        obj = Samples.objects.get(id=payment_type_id)
        obj.delete()
        data  = {
            "status":"ok",
            "message":"deleted",
            }
        return Response(data=data, status=status.HTTP_200_OK)

