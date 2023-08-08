from django.urls import path, include
from .views import SignUp, Profile, follow, unfollow

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name="signup"),
    path('profile/<str:username>/', Profile.as_view(), name="profile"),
    path('follow/<str:username>/', follow, name="follow"),
    path('unfollow/<str:username>/', unfollow, name="unfollow"),
]