from django.urls import path
from .views import Index, TopicDetail, PostDetail, NewPost, NewComment

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('topic/<str:uuid>/', TopicDetail.as_view(), name="topicDetail"),
    path('post/new-post/', NewPost.as_view(), name="newPost"),
    path('post/<str:slug>/', PostDetail.as_view(), name="postDetail"),
    path('comment/<str:uuid>/', NewComment.as_view(), name="newComment"),
]