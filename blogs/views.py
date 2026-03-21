from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm, EditPostForm
from .models import Post, Comment

# Create your views here.
@login_required
def home(request):

    posts = Post.objects.all()

    return render(request,'blogs/home.html', {'posts': posts})

@login_required
def createpost(request):

    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('blogs:home')
        
        else:
            print(form.errors)

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

@login_required
def deletecomment(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)

    if request.user != comment.author and request.user != comment.post.author:
        return redirect('blogs:home')

    post_id = comment.post.id
    comment.delete()

    return redirect('blogs:postdetail', post_id=post_id)

@login_required
def myposts(request):
    posts = Post.objects.filter(author=request.user).order_by('-datecreated')

    return render(request, 'blogs/myposts.html', {
        'posts': posts
    })

@login_required
def deletepost(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user == post.author:
        post.delete()

    return redirect('blogs:myposts')

@login_required
def editpost(request,post_id):
    post = get_object_or_404(Post, id=post_id)

    # 🔐 Security check
    if request.user != post.author:
        return redirect('blogs:home')

    if request.method == "POST":
        form = EditPostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('blogs:postdetail', post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'blogs/editpost.html', {
        'form': form,
        'post': post
    })