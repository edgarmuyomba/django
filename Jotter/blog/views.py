from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Topic

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
        context = {'posts': posts, 'topic': topic}
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