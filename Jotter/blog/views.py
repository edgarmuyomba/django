from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Topic, Comment, Like
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, JsonResponse


class Index(ListView):
    model = Post 
    template_name = "blog/index.html"

class TopicDetail(DetailView):
    model = Topic 
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    template_name = "blog/topicDetail.html"

    def get(self, request, *args, **kwargs):
        topic = super(TopicDetail, self).get_object()
        posts = topic.post_set.all()
        followers = topic.followers.all()
        subscribed = False 
        if topic in request.user.topics.all():
            subscribed = True 
        context = {'posts': posts, 'topic': topic, 'subscribed': subscribed, 'followers': followers}
        return render(request, self.template_name, context)
    
class PostDetail(DetailView):
    model = Post 
    template_name = "blog/postDetail.html"
    slug_field = "slug"

    def get(self, request, *args, **kwargs):
        post = super(PostDetail, self).get_object()
        comments = post.comment_set.all()
        context = {'post': post, 'comments': comments}
        return render(request, self.template_name, context)
    
class NewPost(CreateView):
    form_class = PostForm
    model = Post
    success_url = reverse_lazy("blog:index")
    template_name = "blog/newPost.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.author = request.user
            newPost.save()
            return HttpResponseRedirect(self.success_url)
        return self.form_invalid(form)
    
class NewComment(CreateView):
    form_class = CommentForm
    model = Comment 
    template_name = "blog/newComment.html"
    
    def form_valid(self, form):
        post_uuid = self.kwargs.get('uuid')
        post = get_object_or_404(Post, uuid=post_uuid)
        form.instance.post = post
        form.instance.author = self.request.user
        return super(NewComment, self).form_valid(form)
    
    def get_success_url(self):
        post_uuid = self.kwargs['uuid']
        post = get_object_or_404(Post, uuid=post_uuid)
        return reverse("blog:postDetail", args=[post.slug])

def likePost(request, uuid):
    post = get_object_or_404(Post, uuid=uuid)
    if Like.objects.filter(user=request.user).exists():
        post.likes.remove(request.user)
    else:
        newLike = Like(owner=request.user, post=post)
        newLike.save()
    post.save()

def subscribe(request, uuid):
    topic = get_object_or_404(Topic, uuid=uuid)
    request.user.topics.add(topic)
    return JsonResponse({'message': 'success'})

def unsubscribe(request, uuid):
    topic = get_object_or_404(Topic, uuid=uuid)
    request.user.topics.remove(topic)
    return JsonResponse({'message': 'success'})