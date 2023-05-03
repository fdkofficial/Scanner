from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate

class DepartmentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Samples
        fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

