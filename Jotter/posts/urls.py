from django.urls import path 
from . import views 

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<str:uuid>/', views.likePost, name='likePost'),
    path('post/<str:uuid>/<slug:slug>/', views.postDetails, name='postDetails'),
    path('delete/<str:uuid>/', views.deletePost, name='deletePost'),
    path('create-a-new-post/', views.createPost.as_view(), name='createPost'),
    path('edit-Post/<str:uuid>/', views.editPost.as_view(), name='editPost'),
    path('reply/<str:postUUID>/', views.reply.as_view(), name='reply'),
    path('reply/<str:postUUID>/<str:parentUUID>/', views.reply.as_view(), name='reply'),
    path('delete-comment/<str:postUUID>/<str:comUUID>/', views.deleteComment, name='deleteComment'),
    path('search/', views.search, name='search'),
    path('search/?q=<slug:slug>/', views.searchSlug, name='searchSlug'),
    path('category/<str:cat>/<str:uuid>/', views.category, name='category'),
    path('tag/<str:sTag>/', views.tag, name='tag'),
]