from django.shortcuts import render
from .forms import SignUpForm
from django.views.generic import CreateView, DetailView
from .models import CustomUser
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

class SignUp(CreateView):
    form_class = SignUpForm
    model = CustomUser
    success_url = reverse_lazy('blog:index')
    template_name = 'registration/signup.html'

class Profile(DetailView):
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'registration/profile.html'

    def get(self, request, *args, **kwargs):
        profile = super(Profile, self).get_object()
        posts = profile.post_set.all()
        comments = profile.comment_set.all()
        topics = profile.topics.all()
        followers = profile.followers.all()
        following = profile.following.all()
        likedPosts = profile.likedPosts.all()
        follow = False
        if profile in request.user.following.all():
            follow = True
        context = {'profile': profile, 'posts': posts, 'comments': comments, 'topics': topics, 'follow': follow, 'followers': followers, 'following': following, 'likedPosts': likedPosts}
        return render(request, self.template_name, context)
    
def follow(request, username):
    user = get_object_or_404(CustomUser, username=username)
    request.user.following.add(user)
    return JsonResponse({'message': 'success'})

def unfollow(request, username):
    user = get_object_or_404(CustomUser, username=username)
    request.user.following.remove(user)
    return JsonResponse({'message': 'success'})