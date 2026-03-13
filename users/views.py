from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.
def home(request):
    return render(request,'users/home.html')

def login(request):
    return render(request, 'users/login.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('users:login')
        
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {"form": form})