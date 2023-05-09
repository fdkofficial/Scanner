from django.urls import path,include
from . import views
urlpatterns = [
    path('collect-sample-data/',views.collect_samples,name='collect-sample'),
    path('drop-sample-data/',views.drop_samples,name='collect-sample'),
    path('department/',views.department,name='department'),
    path('units/',views.untis,name='units'),
    path('labaratory/',views.labaratory,name='labaratory'),
    path('sample-histories/',views.sample_history,name='sample-histories'),
    path('sample-histories-api/',views.sample_history_data,name='sample-histories-data'),
    path('view-sample-histories/<str:id>',views.view_sample_history,name='sample-histories-data-id'),
]
