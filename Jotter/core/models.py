from django.db import models
from uuid import uuid4

class Topic(models.Model):
    title = models.CharField(max_length=25)
    followers = models.IntegerField()

    def __str__(self):
        return self.title

class Post(models.Model):
    uuid = models.UUIDField(default=uuid4)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=155)
    dateAdded = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField()

    def __str__(self):
        return f'{self.content[:50]}...'
