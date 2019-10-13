from django.db import models

from category.models import Category


class TopicQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def sub_category(self, sub):
        qs = self.filter(category__slug=sub)
        return qs


class TopicManager(models.Manager):
    def get_queryset(self):
        return TopicQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().active()

    def sub_category(self, sub):
        if sub:
            return self.all().sub_category(sub)
        else:
            return self.all()


class Topic(models.Model):
    title = models.CharField(max_length=120)
    title_pic = models.CharField(max_length=120)
    # slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, related_name='category_topics', on_delete=models.CASCADE)
    desc = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TopicManager()

    def __str__(self):
        return self.title
