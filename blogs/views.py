from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
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

@login_required
def postdetail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect('blogs:postdetail', post_id=post.id)

    else:
        form = CommentForm()

    return render(request,'blogs/postdetail.html', {'post': post,'form': form,'comments': comments})