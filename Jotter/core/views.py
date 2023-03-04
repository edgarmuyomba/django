from django.shortcuts import render
from .models import Post, Topic

def index(request):
    posts = Post.objects.all()
    topics = Topic.objects.all()
    context = {'posts': posts, 'topics': topics}
    return render(request, 'core/index.html', context)
