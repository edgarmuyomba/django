from django.contrib import admin
from .models import CustomUser

class userAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']

admin.site.register(CustomUser, userAdmin)
