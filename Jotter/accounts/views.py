from django.shortcuts import render
from .forms import SignUpForm
from django.views.generic import CreateView, DetailView
from .models import CustomUser
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

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
        context = {'profile': profile, 'posts': posts, 'comments': comments, 'topics': topics}
        return render(request, self.template_name, context)