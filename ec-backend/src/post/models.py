from django.db import models

from category.models import Category
from topic.models import Topic


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    title_pic = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    share_num = models.IntegerField()
    share_id = models.IntegerField()
    location = models.CharField(max_length=50)
    type = models.IntegerField()
    category = models.ForeignKey(Category, related_name='category_posts', on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topic, related_name='topic_posts')
    public = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



