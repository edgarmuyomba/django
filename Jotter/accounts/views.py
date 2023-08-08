from django.shortcuts import render
from .forms import SignUpForm
from django.views.generic import CreateView 
from .models import CustomUser
from django.urls import reverse_lazy

class SignUp(CreateView):
    form_class = SignUpForm
    model = CustomUser
    success_url = reverse_lazy('blog:index')
    template_name = 'registration/signup.html'
