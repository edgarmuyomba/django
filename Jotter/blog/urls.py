from django.urls import path
from django.views.generic import TemplateView
from .views import Index, TopicDetail, PostDetail

app_name = 'blog'

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('topic/<str:uuid>/', TopicDetail.as_view(), name="topicDetail"),
    path('post/<str:slug>/', PostDetail.as_view(), name="postDetail"),
]