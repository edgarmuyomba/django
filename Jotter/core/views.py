from django.shortcuts import render, redirect
from .models import Post, Topic
from django.views.generic import View
from .forms import postForm

def index(request):
    posts = Post.objects.all().order_by('-dateAdded')
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

def postDetails(request, uuid, slug):
    post = Post.objects.get(uuid=uuid)
    tags = post.tags.split(',')
    context = {'post': post, 'tags': tags}
    return render(request, 'core/postDetails.html', context)

def deletePost(request, uuid):
    post = Post.objects.get(uuid=uuid)
    post.delete()
    return redirect('core:index')

class createPost(View):
    template_name = 'core/createPost.html'
    form = postForm

    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
        else: 
            return 