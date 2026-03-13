from django.urls import path
from .views import home, createpost, postdetail

app_name = 'blogs'

urlpatterns = [
    path('',home,name='home'),
    path('createpost/',createpost, name = 'createpost'),
    path('post/<int:post_id>', postdetail, name='postdetail')
]