from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.registerView.as_view(), name='register'),
    path('login/', views.loginView.as_view(), name='login'),
    path('logout/', views.logOutView, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    # path('profile/edit/', views.editProfile, name='editProfile'),
    # path('profile/edit/password/', views.editPassword, name='editPassword'),
    # path('profile/resetPassword/', views.resetPassword, name='resetPassword'),
]