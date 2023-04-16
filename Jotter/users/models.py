from django.db import models
from django.contrib.auth.models import AbstractUser
from posts.models import Topic

class CustomUser(AbstractUser):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    profilePic = models.ImageField(upload_to='profilePics', blank=True)
    following = models.ManyToManyField('self', blank=True)
    followers = models.ManyToManyField('self', blank=True)
    socialLinks = models.TextField(blank=True)
    topics = models.ManyToManyField(Topic, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstName', 'lastName']

    def __str__(self):
        return self.firstName
    pass
