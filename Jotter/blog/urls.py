from django.urls import path
from .views import Index, TopicDetail, PostDetail, NewPost, NewComment, likePost, subscribe, unsubscribe

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('topic/<str:uuid>/', TopicDetail.as_view(), name="topicDetail"),
    path('post/new-post/', NewPost.as_view(), name="newPost"),
    path('post/<str:slug>/', PostDetail.as_view(), name="postDetail"),
    path('comment/<str:uuid>/', NewComment.as_view(), name="newComment"),
    path('like/<str:uuid>/', likePost, name="likePost"),
    path('subscribe/<str:uuid>/', subscribe, name="subscribe"),
    path('unsubscribe/<str:uuid>/', unsubscribe, name="unsubscribe"),
]