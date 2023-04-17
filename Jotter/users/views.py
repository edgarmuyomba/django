from django.shortcuts import render, redirect
from .forms import signupForm, loginForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View
from .models import CustomUser

class loginView(View):
    def get(self, request):
        form = loginForm()
        return render(request, 'users/login.html', {'form': form})
    def post(self, request):
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('posts:index')
            else:
                return render(request, 'users/login.html', {'form': form})
        else:
            return render(request, 'users/login.html', {'form': form})

class registerView(View):
    def get(self, request):
        form = signupForm()
        return render(request, 'users/signup.html', {'form': form})
    def post(self, request):
        form = signupForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request, user)
            return redirect('posts:index')
        else:
            return render(request, 'users/signup.html', {'form': form})

def logOutView(request):
    logout(request)
    return redirect('posts:index')

def profile(request, username):
    user = CustomUser.objects.get(username=username)
    context = {'user': user}
    return render(request, 'users/profile.html', context)
