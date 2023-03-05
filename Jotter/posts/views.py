from django.shortcuts import render, redirect
from .models import Post, Topic
from django.views.generic import View

def index(request):
    posts = Post.objects.all().order_by('-dateAdded')
    topics = Topic.objects.all()
    context = {'posts': posts, 'topics': topics}
    return render(request, 'posts/index.html', context)

def likePost(request, uuid):
    post = Post.objects.get(uuid=uuid)
    if post.likes:
        post.likes += 1
    else:
        post.likes = 1
    post.save()
    return redirect('posts:index')

def postDetails(request, uuid, slug):
    post = Post.objects.get(uuid=uuid)
    tags = post.tags.split(',')
    context = {'post': post, 'tags': tags}
    return render(request, 'posts/postDetails.html', context)

def deletePost(request, uuid):
    post = Post.objects.get(uuid=uuid)
    post.delete()
    return redirect('posts:index')

class createPost(View):
    template_name = 'posts/createPost.html'

    def get(self, request):
        topics = Topic.objects.all()
        return render(request, self.template_name, {'topics': topics})
    
    def post(self, request):
        topic = request.POST['topic'] 
        topic = Topic.objects.get(title=topic)
        pTitle = request.POST['title']
        text = request.POST['text']
        tags = request.POST['tags']
        newPost = Post.objects.create(topic=topic, title=pTitle, text=text, tags=tags)
        newPost.save()
        return redirect('posts:index')

class editPost(View):
    pass