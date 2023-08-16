from django.shortcuts import render
from .forms import SignUpForm
from django.views.generic import CreateView, DetailView
from .models import CustomUser
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages

class SignUp(CreateView):
    form_class = SignUpForm
    model = CustomUser
    success_url = reverse_lazy('blog:index')
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            return self.form_invalid(form)

@method_decorator(login_required, name="dispatch")
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
        follow = False
        if request.user in profile.followers.all():
            follow = True
        context = {'profile': profile, 'posts': posts, 'comments': comments, 'topics': topics, 'follow': follow, 'followers': followers, 'following': following}
        return render(request, self.template_name, context)
    
@login_required
def follow(request, username):
    user = get_object_or_404(CustomUser, username=username)
    user2 = get_object_or_404(CustomUser, username=request.user.username)
    user2.follow(user)
    return JsonResponse({'message': 'success'})

@login_required
def unfollow(request, username):
    user = get_object_or_404(CustomUser, username=username)
    user2 = get_object_or_404(CustomUser, username=request.user.username)
    user2.unfollow(user)
    return JsonResponse({'message': 'success'})

class ProfileDetails(DetailView):
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get(self, request, *args, **kwargs):
        profile = super(ProfileDetails, self).get_object()
        posts = profile.post_set.all().count()
        followers = profile.followers.all().count()
        return JsonResponse({'posts': posts, 'followers': followers})