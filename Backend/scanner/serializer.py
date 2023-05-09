from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        units = Unit.objects.filter(department=instance.id)
        units_ser = UnitSerializer(units,many=True).data
        response['units'] = units_ser
        return response

class SamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        origins = SampleData.objects.filter(sample_no__in=[instance.id])
        origin_ser = SampleDataSerializer(origins,many=True).data
        response['origin'] = origin_ser
        dest = DropSampleData.objects.filter(sample_no__in=[instance.id])
        dest_ser = DropSampleDataSerializer(dest,many=True).data
        response['destination'] = dest_ser
        
        return response


class SampleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleData
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['collector_user']= f"{instance.collector_user.first_name} {instance.collector_user.last_name}" if instance.collector_user else ""
        response['origin']= instance.origin.name if instance.origin else ""
        response['sample_no']= [ i.sample_no for i in instance.sample_no.all() ] if instance.sample_no else []
        # response['department']= instance.department.name if instance.department else ""
        return response

class DropSampleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DropSampleData
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['reciever_user']= f"{instance.reciever_user.first_name} {instance.reciever_user.last_name}" if instance.reciever_user else ""
        response['destination']= instance.destination.name if instance.destination else ""
        # response['department']= instance.department.name if instance.department else ""
        return response



class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class LaberatorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laberatory
        fields = '__all__'


