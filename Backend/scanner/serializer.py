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
        units_ser = UnitSerializer(units,many=True)
        response['units'] = units_ser
        return response

class SamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = '__all__'


class SampleDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleData
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class LaberatorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laberatory
        fields = '__all__'


