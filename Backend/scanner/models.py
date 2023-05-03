from django.db import models

from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=255)

# Create your models here.
class Samples(models.Model):
    sample_no = models.CharField(max_length=255,null=True,blank=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    origin = models.CharField(max_length=255,null=True,blank=True)
    destination= models.CharField(max_length=255,null=True,blank=True)
    collect_date = models.DateTimeField(auto_now=True)
    drop_of_date = models.DateTimeField()
    reciever_id = models.CharField(max_length=1000)
    collector_user = models.ForeignKey(User,on_delete=models.CASCADE)

class Building(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)