from django.contrib import admin
from .models import *

class topicInline(admin.TabularInline):
    model = CustomUser.topics.through 

class userAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    inlines = [topicInline]

admin.site.register(CustomUser, userAdmin)

class RelationAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user']

admin.site.register(FollowerRelation, RelationAdmin)
