from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

# Create your views here.
@login_required
def home(request):

    posts = Post.objects.all()

    return render(request,'blogs/home.html', {'posts': posts})

@login_required
def createpost(request):

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('blogs:home')

    else:
        form = PostForm()

    return render(request,'blogs/createpost.html', {'form': form})