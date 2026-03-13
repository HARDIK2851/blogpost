from django.urls import path
from .views import home, createpost

app_name = 'blogs'

urlpatterns = [
    path('',home,name='home'),
    path('createpost/',createpost, name = 'createpost')
]