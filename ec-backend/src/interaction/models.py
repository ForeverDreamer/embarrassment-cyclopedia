from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model

from content.models import Post

User = get_user_model()

LIKE_STATUS = (
    ('like', '顶'),
    ('unlike', '踩'),
    ('cancel', '取消'),
)


# 顶踩
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


# 评论
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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


# 黑名单
class BlockUser(models.Model):
    owner = models.ForeignKey(User, related_name='blocking_set', on_delete=models.CASCADE)
    blocked = models.ForeignKey(User, related_name='blocked_set', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'BlockUser'
        verbose_name_plural = 'BlockUsers'

    def __str__(self):
        return '{owner}屏蔽{blocked}'.format(owner=self.owner.username, blocked=self.blocked.username)


class FollowUserQuerySet(models.query.QuerySet):
    pass


class FollowUserManager(models.Manager):
    def get_queryset(self):
        return CommentQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all()

    def friends(self, owner):
        # 我关注或关注我的用户
        # qlookup = Q(owner=owner) | Q(followed=owner)
        # 我关注的用户
        following_qs = self.all().filter(owner=owner)
        following_user_set = {follow_info.followed for follow_info in list(following_qs)}
        # 关注我用户
        fans_qs = self.all().filter(followed=owner)
        fans_user_set = {follow_info.owner for follow_info in list(fans_qs)}
        friend_set = {following_user for following_user in following_user_set if following_user in fans_user_set}
        # for following_user in following_user_list:
        #     if following_user in fans_user_list:
        #         friend_list.append(following_user)

        return list(friend_set)

    def fans(self, owner):
        # 关注我用户
        fans_qs = self.all().filter(followed=owner)
        fans_user_list = [follow_info.owner for follow_info in list(fans_qs)]

        return fans_user_list

    def follows(self, owner):
        # 我关注的用户
        follws_qs = self.all().filter(owner=owner)
        follows_user_list = [follow_info.followed for follow_info in list(follws_qs)]

        return follows_user_list


# 关注
class FollowUser(models.Model):
    owner = models.ForeignKey(User, related_name='follow_set', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='fans', on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = FollowUserManager()

    class Meta:
        verbose_name = 'FollowUser'
        verbose_name_plural = 'FollowUsers'

    def __str__(self):
        return '{owner}关注{blocked}'.format(owner=self.owner.username, blocked=self.followed.username)


# 用户反馈
class Feedback(models.Model):
    # 客服人员
    customer_service = models.ForeignKey(User, related_name='answer_set', on_delete=models.CASCADE)
    # 反馈客户
    owner = models.ForeignKey(User, related_name='ask_set', on_delete=models.CASCADE)
    question = models.TextField()
    solved = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'FeedBack'
        verbose_name_plural = 'FeedBacks'

    def __str__(self):
        return self.question[:10]


class AppUpdateQuerySet(models.query.QuerySet):
    def online(self):
        return self.filter(online=True)


class AppUpdateManager(models.Manager):
    def get_queryset(self):
        return AppUpdateQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().online()


# App更新
class AppUpdate(models.Model):
    url = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    online = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)

    objects = AppUpdateManager()

    class Meta:
        verbose_name = 'AppUpdate'
        verbose_name_plural = 'AppUpdates'

    def __str__(self):
        return self.version
