from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name="signup"),
    path('profile/<str:username>/', Profile.as_view(), name="profile"),
    path('follow/<str:username>/', follow, name="follow"),
    path('unfollow/<str:username>/', unfollow, name="unfollow"),
    path('profileDetails/<str:username>/', ProfileDetails.as_view(), name="profileDetails"),
]