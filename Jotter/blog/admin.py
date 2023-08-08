from django.contrib import admin
from .models import Topic, Post, Comment 

class TopicAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Topic, TopicAdmin)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    list_display = ['title', 'topic', 'author', 'tags']

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Comment, CommentAdmin)
