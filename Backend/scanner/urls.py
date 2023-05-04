from django.urls import path,include
from . import views
urlpatterns = [
    path('sample-data/',views.collect_samples,name='collect-sample'),
    path('department/',views.department,name='department'),
    path('labaratory/',views.labaratory,name='labaratory'),
]
