from django.urls import path
from django.contrib.auth.views import LoginView
from .views import home, signup

app_name = 'users'

urlpatterns = [
    path('',home,name='home'),
    # path('login',login,name='login'),
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('signup/',signup,name='signup')
]