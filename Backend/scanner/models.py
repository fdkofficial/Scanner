from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.contrib.auth.models import User

class Department(models.Model):
    name = models.CharField(max_length=255)
    dep_id = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)
    
import random

def random_string():
    return str(random.randint(100000, 9999999))
class Unit(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    unit_no = models.CharField(max_length=255,default=random_string)
    qr_image = models.ImageField(blank=True, null=True, upload_to='QRCode')
    def __str__(self):
        return str(self.department.name) + ":- " + str(self.name)
    def save(self, *args, **kwargs):
        qr_image = qrcode.make(self.unit_no)
        qr_offset = Image.new('RGB', (310, 310), 'white')
        draw_img = ImageDraw.Draw(qr_offset)
        qr_offset.paste(qr_image)
        file_name = f'{self.name}-{self.id}qr.png'
        stream = BytesIO()
        qr_offset.save(stream, 'PNG')
        self.qr_image.save(file_name, File(stream), save=False)
        qr_offset.close()
        super().save(*args, **kwargs)

class Sample(models.Model):
    sample_no = models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now=True)
    collected = models.BooleanField(default=False)
    # name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.sample_no)



class Laberatory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)

# Create your models here.
class SampleData(models.Model):
    sample_no = models.ManyToManyField(Sample,null=True)
    origin = models.ForeignKey(Unit,on_delete=models.CASCADE,null=True,blank=True)
    collect_date = models.DateTimeField(auto_now=True)
    collector_user = models.ForeignKey(User,on_delete=models.CASCADE)

class DropSampleData(models.Model):
    sample_no = models.ManyToManyField(Sample,null=True)
    destination= models.ForeignKey(Laberatory,on_delete=models.CASCADE,null=True,blank=True)
    drop_of_date = models.DateTimeField()
    reciever_id = models.CharField(max_length=1000)
    reciever_user = models.ForeignKey(User,on_delete=models.CASCADE)

# class sampleshistory(models.Model):
#     collect_data= models.ForeignKey(SampleData,on_delete=models.CASCADE,null=True,blank=True)
#     drop = models.ForeignKey(DropSampleData,on_delete=models.CASCADE,null=True,blank=True)
    