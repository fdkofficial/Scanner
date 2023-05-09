from csv import field_size_limit
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# from employee.models import CustomUser as User
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

from scanner.serializer import SampleData,SampleDataSerializer

class LogsDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    def to_representation(self, instance):
        response = super().to_representation(instance)
        logs = SampleData.objects.filter(collector_user=instance.id)
        print(logs)
        logs_ser = SampleDataSerializer(logs,many=True).data
        response['logs'] = logs_ser
        return response


