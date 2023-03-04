from django.shortcuts import render, redirect
from .models import Post, Topic

def index(request):
    posts = Post.objects.all()
    topics = Topic.objects.all()
    context = {'posts': posts, 'topics': topics}
    return render(request, 'core/index.html', context)

def likePost(request, uuid):
    post = Post.objects.get(uuid=uuid)
    if post.likes:
        post.likes += 1
    else:
        post.likes = 1
    post.save()
    return redirect('core:index')

def postDetails(request, uuid):
    post = Post.objects.get(uuid=uuid)
    return render(request, 'core/postDetails.html', {'post': post})