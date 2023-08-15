from django.db import models
from django.contrib.auth.models import AbstractUser
from blog.models import Topic

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    following = models.ManyToManyField('self', blank=True, symmetrical=False, related_name="followers", through='FollowerRelation')
    socialLinks = models.TextField(blank=True)
    topics = models.ManyToManyField(Topic, blank=True, related_name='subscribers')

    def __str__(self):
        return self.username
    
    def follow(self, other):
        if not self == other:
            relation = FollowerRelation.objects.get_or_create(from_user=self, to_user=other)
            return relation
    
    def unfollow(self, other):
        relation = FollowerRelation.objects.get(from_user=self, to_user=other)
        if relation:
            relation.delete()
    
class FollowerRelation(models.Model):
    from_user = models.ForeignKey(CustomUser, related_name="from_user_relations", on_delete=models.CASCADE)
    to_user = models.ForeignKey(CustomUser, related_name="to_user_relations", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('from_user', 'to_user')

