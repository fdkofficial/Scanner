from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([Sample,Department,Laberatory,Unit])

class SampleDataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SampleData._meta.fields]

class DropSampleDataAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DropSampleData._meta.fields]


admin.site.register(SampleData,SampleDataAdmin)
admin.site.register(DropSampleData,DropSampleDataAdmin)