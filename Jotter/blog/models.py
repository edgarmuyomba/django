from django.db import models
from django.conf import settings
from uuid import uuid4
from django.template.defaultfilters import slugify

class Topic(models.Model):
    title = models.CharField(max_length=25)
    uuid = models.UUIDField(default=uuid4)

    def __str__(self):
        return self.title

class Post(models.Model):
    uuid = models.UUIDField(default=uuid4, auto_created=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=False)
    tags = models.CharField(max_length=50)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, through='LikeRelation', related_name='likedPosts')

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-dateAdded',)
    
    def save(self, *args, **kwargs): 
        if not self.slug:
            slugList = self.title.split(' ')
            self.slug = slugify(slugList[:5])
        return super().save(*args, **kwargs)
    
    def like(self, user):
        relation = LikeRelation.objects.get_or_create(author=user, post=self)
        return relation
    
    def unlike(self, user):
        relation = LikeRelation.objects.get(author=user, post=self)
        if relation:
            relation.delete()
    
class LikeRelation(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('author', 'post')

    def __str__(self):
        return f"'{self.author}' likes '{self.post}'"

class Comment(models.Model):
    uuid = models.UUIDField(default=uuid4)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    text = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True, auto_created=True)
    
    def __str__(self):
        return ' '.join(self.text.split(' ')[:5])
    
    class Meta:
        ordering = ['-dateAdded']