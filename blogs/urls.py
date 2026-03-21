from django.urls import path
from .views import home, createpost, postdetail, deletecomment, myposts

app_name = 'blogs'

urlpatterns = [
    path('',home,name='home'),
    path('createpost/',createpost, name = 'createpost'),
    path('post/<int:post_id>', postdetail, name='postdetail'),
    path('comment/delete/<int:comment_id>/',deletecomment,name='deletecomment'),
    path('myposts/',myposts,name='myposts')
]