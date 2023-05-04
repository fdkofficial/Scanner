from django.db import models

from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=255)
    dep_id = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)


class Unit(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.department.name) + ":- " + str(self.name)

class Sample(models.Model):
    sample_no = models.CharField(max_length=500)
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)



class Laberatory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)

# Create your models here.
class SampleData(models.Model):
    sample_no = models.ManyToManyField(Sample,null=True)
    origin = models.ManyToManyField(Unit,null=True)
    # origin = models.CharField(max_length=255,null=True,blank=True)
    destination= models.ManyToManyField(Laberatory,null=True)
    collect_date = models.DateTimeField(auto_now=True)
    drop_of_date = models.DateTimeField()
    reciever_id = models.CharField(max_length=1000)
    collector_user = models.ForeignKey(User,on_delete=models.CASCADE)
