from csv import field_size_limit
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# from employee.models import CustomUser as User
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'