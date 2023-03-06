from django.db import models
from uuid import uuid4
from django.template.defaultfilters import slugify

class Topic(models.Model):
    title = models.CharField(max_length=25)
    followers = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    uuid = models.UUIDField(default=uuid4, auto_created=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=False)
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
