from django.shortcuts import render, redirect
from .models import Post, Topic, Comment
from django.views.generic import View
from django.template.defaultfilters import slugify
from .forms import postForm
from django.db.models import Q
from django.utils.text import slugify
from django.views.generic import ListView


def index(request):
    posts = Post.objects.all().order_by('-likes')
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
    comments = post.comment_set.all().filter(parent=None)
    numOfComments = len(post.comment_set.all())
    context = {'post': post, 'tags': tags,
               'comments': comments, 'numOfComments': numOfComments}
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
        slug = slugify(pTitle)
        text = request.POST['text']
        tags = request.POST['tags']
        newPost = Post.objects.create(
            topic=topic, title=pTitle, text=text, slug=slug, tags=tags)
        newPost.save()
        return redirect('posts:index')


class editPost(View):
    template_name = 'posts/editPost.html'
    form = postForm

    def get(self, request, uuid):
        post = Post.objects.get(uuid=uuid)
        form = self.form(instance=post)
        context = {'post': post, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, uuid):
        post = Post.objects.get(uuid=uuid)
        form = self.form(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:index')


class reply(View):
    template_name = 'posts/reply.html'

    def get(self, request, postUUID, parentUUID=None):
        post = Post.objects.get(uuid=postUUID)
        parent = None
        if parentUUID:
            parent = Comment.objects.get(uuid=parentUUID)
        context = {'post': post, 'parent': parent}
        return render(request, self.template_name, context)

    def post(self, request, postUUID, parentUUID=None):
        text = request.POST['text']
        fPost = Post.objects.get(uuid=postUUID)
        parent = None
        if parentUUID:
            parent = Comment.objects.get(uuid=parentUUID)
        newReply = Comment(post=fPost, parent=parent, text=text)
        newReply.save()
        return redirect('posts:postDetails', postUUID, fPost.slug)


def deleteComment(request, postUUID, comUUID):
    comment = Comment.objects.get(uuid=comUUID)
    comment.delete()
    post = Post.objects.get(uuid=postUUID)
    return redirect('posts:postDetails', postUUID, post.slug)


def search(request):
    if request.method == 'POST':
        query = request.POST['search']
        slug = slugify(query)
        if slug:
            return redirect('posts:searchSlug', slug)
        
def searchSlug(request, slug):
    query = slug.split('-')
    query = ' '.join(query)
    results = Post.objects.all().filter(
        Q(title__icontains=query) | Q(text__icontains=query)
    )
    context = {'results': results}
    return render(request, 'posts/searchResults.html', context)

def category(request, cat, uuid):
    topic = Topic.objects.get(uuid=uuid)
    posts = topic.post_set.all()
    context = {'topic': topic, 'posts': posts}
    return render(request, 'posts/category.html', context)

def tag(request, sTag):
    posts = Post.objects.all().filter(tags__icontains=sTag)
    context = {'posts': posts, 'tag': sTag}
    return render(request, 'posts/tag.html', context)
