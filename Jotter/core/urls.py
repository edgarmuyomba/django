from django.urls import path 
from . import views 

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<str:uuid>/', views.likePost, name='likePost'),
    path('post/<str:uuid>/', views.postDetails, name='postDetails'),
]