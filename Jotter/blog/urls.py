from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('topic/<str:uuid>/', TopicDetail.as_view(), name="topicDetail"),
    path('post/new-post/', NewPost.as_view(), name="newPost"),
    path('post/<str:slug>/', PostDetail.as_view(), name="postDetail"),
    path('comment/<str:uuid>/', newComment, name="newComment"),
    path('like/<str:uuid>/', like, name="like"),
    path('unlike/<str:uuid>/', unlike, name="unlike"),
    path('subscribe/<str:uuid>/', subscribe, name="subscribe"),
    path('unsubscribe/<str:uuid>/', unsubscribe, name="unsubscribe"),
    path('search/', search, name='search')
]