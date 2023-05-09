from django.shortcuts import render


# Create your views here.
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from .serializer import *
import datetime

# Create your views here.
@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def collect_samples(request):
    if request.method == 'GET':

        obj = SampleData.objects.all()
        serializer = SampleDataSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        sample_list = []
        request.data['collector_user'] = request.user.id
        request.data['collect_date'] = datetime.datetime.now()
        for i in request.data['sample_no']:
            fil = Sample.objects.filter(sample_no=i).last()
            if fil:
                fil.collected = True
                fil.save()
                sample_list.append(fil.id)
            else:
                sample = Sample(sample_no=i)
                sample.collected = True
                sample.save()
                sample_list.append(sample.id)
        request.data['sample_no'] = sample_list
        request.data['collector_user'] = request.user.id
        serializer = SampleDataSerializer(data=request.data)
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
        obj = SampleData.objects.get(id=payment_type_id)
        serializer = SampleDataSerializer(obj,data=request.data)
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

@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def drop_samples(request):
    if request.method == 'GET':

        obj = DropSampleData.objects.all()
        serializer = DropSampleDataSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        sample_list = []
        request.data['reciever_user'] = request.user.id
        request.data['drop_of_date'] = datetime.datetime.now()
        error_ = None
        for i in request.data['sample_no']:
            fil = Sample.objects.filter(sample_no=i).last()
            if fil and fil.collected:
                # sample_list.append(fil.id)
                fil.collected = False
                fil.save()
                sample_list.append(fil.id)
            elif not fil.collected:
                error_ = i+" Not Collected Yet"
                # sample = Sample(sample_no=i,collected=False)
                # sample.save()
                # return Response(data=i+" "+"Not Collected Yet",status=status.HTTP_400_BAD_REQUEST)
            else:
                error_ = i+" Not Collected Yet"
                # return Response(data=data,status=status.HTTP_400_BAD_REQUEST)
            
        request.data['sample_no'] = sample_list
        request.data['collector_user'] = request.user.id
        if error_ is not None:
                data = error_
                return Response(data=data,status=status.HTTP_200_OK)
        serializer = DropSampleDataSerializer(data=request.data)
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
        obj = DropSampleData.objects.get(id=payment_type_id)
        serializer = DropSampleDataSerializer(obj,data=request.data)
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



@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def department(request):
    if request.method == 'GET':

        obj = Department.objects.all()
        serializer = DepartmentSerializer(obj,many=True)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def untis(request):
    if request.method == 'GET':
        code = request.GET.get('code')
        
        obj = Unit.objects.filter(unit_no=code).last()
        print(obj)
        
        serializer = UnitSerializer(obj)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)


from django.contrib.auth.models import User
from login.serializer import LogsDetailsSerializer


@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logs(request):
    if request.method == 'GET':
        obj = User.objects.filter(id=request.user.id).last()
        serializer = LogsDetailsSerializer(obj)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)



from django.shortcuts import render
def sample_history(request):
    if request.method == 'GET':
        return render(request,'sample.html')
    

from django.shortcuts import render
def view_sample_history(request,id):
    sample_id = id
    if request.method == 'GET':
        return render(request,'viewsample.html',{'sample_id':sample_id})
    

   
@api_view(['GET','POST','PUT','DELETE'])
def sample_history_data(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if id is not None:
            obj = Sample.objects.filter(id=id)
        else:
            obj = Sample.objects.all()
        obj_ser = SamplesSerializer(obj,many=True).data
        
        return Response(data=obj_ser)




@api_view(['GET','POST','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def labaratory(request):
    if request.method == 'GET':
        obj = Laberatory.objects.all()
        serializer = LaberatorySerializer(obj,many=True)
        code = request.GET.get("code")
        if code is not None:
            obj = Laberatory.objects.filter(lab_id=code).last()
            serializer = LaberatorySerializer(obj)
        data = {
            "satus":"ok",
            "message":"successfull",
            "data": serializer.data
        }
        return Response(data=data,status=status.HTTP_200_OK)

