from django.contrib import admin
from .models import Topic, Post, Comment

admin.site.register(Topic)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)