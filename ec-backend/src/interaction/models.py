from django.db import models

from content.models import Post

LIKE_STATUS = (
    ('like', '顶'),
    ('unlike', '踩'),
    ('cancel', '取消'),
)


class LikeInfo(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=LIKE_STATUS)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'LikeInfo'
        verbose_name_plural = 'LikeInfos'

    def __str__(self):
        return self.post.title


class CommentQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class CommentManager(models.Manager):
    def get_queryset(self):
        return CommentQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().active()


class Comment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text[:10]