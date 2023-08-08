from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import Topic, Post, Comment

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    profilePic = models.ImageField(upload_to='profilePics', blank=True)
    following = models.ManyToManyField('self', blank=True)
    followers = models.ManyToManyField('self', blank=True)
    socialLinks = models.TextField(blank=True)
    topics = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return self.username