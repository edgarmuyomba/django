from django.contrib import admin
from .models import Topic, Post, Comment 

class TopicAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Topic, TopicAdmin)

class PostAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Comment, CommentAdmin)