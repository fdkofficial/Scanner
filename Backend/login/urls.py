from django.urls import re_path as url
from .views import Signupapi, Signuppage, loginView, loginpage, logoutView

urlpatterns = [
    url('login/', loginView,
        name='login'),
    url('logout/', logoutView,
        name='logout'),
    url('signup/', Signupapi,
        name='sign-up')
]
