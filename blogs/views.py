from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request,'blogs/home.html')

@login_required
def createpost(request):
    return render(request,'blogs/createpost.html')