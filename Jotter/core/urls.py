from django.urls import path 
from . import views 

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<str:uuid>/', views.likePost, name='likePost'),
    path('post/<str:uuid>/<slug:slug>/', views.postDetails, name='postDetails'),
    path('delete/<str:uuid>/', views.deletePost, name='deletePost'),
    path('create-a-new-post/', views.createPost.as_view(), name='createPost'),
]