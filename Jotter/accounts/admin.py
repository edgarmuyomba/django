from django.contrib import admin
from .models import CustomUser

class topicInline(admin.TabularInline):
    model = CustomUser.topics.through 

class userAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    inlines = [topicInline]

admin.site.register(CustomUser, userAdmin)
