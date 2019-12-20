from django.conf import settings
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist

from .utils import broadcast_msg_to_chat, trigger_welcome_message


class ChannelName(models.Model):
    channel_name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class PrivateChatQuerySet(models.query.QuerySet):
    pass


class PrivateChatManager(models.Manager):
    def get_queryset(self):
        return PrivateChatQuerySet(self.model, using=self._db)

    def by_user(self, user):
        qlookup = Q(first=user) | Q(second=user)
        # qlookup2 = Q(first=user) & Q(second=user)
        # qs = self.get_queryset().filter(qlookup).exclude(qlookup2).distinct()
        qs = self.get_queryset().filter(qlookup).distinct()
        return qs

    def get_or_new(self, user, other_user_id):  # get_or_create
        qs = User.objects.filter(id=other_user_id)
        if not qs.exists():
            raise ObjectDoesNotExist('用户不存在')
        other_user = qs.first()
        if user == other_user:
            raise ValidationError('不能和自己私聊')
        qlookup1 = Q(first=user) & Q(second=other_user)
        qlookup2 = Q(first=other_user) & Q(second=user)
        qs = self.get_queryset().filter(qlookup1 | qlookup2).distinct()
        if qs.exists():
            print('返回已有私聊')
            return qs.first(), False
        # elif qs.count() > 1:
        #     return qs.order_by('timestamp').first(), False
        else:
            obj = self.model(
                first=user,
                second=other_user
            )
            obj.save()
            print('创建私聊')
            return obj, True


class PrivateChat(models.Model):
    first = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_as_first_msgs')
    second = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='chat_as_second_msgs')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PrivateChatManager()

#     @property
#     def room_group_name(self):
#         return f'chat_{self.id}'
#
#     def broadcast(self, msg=None):
#         if msg is not None:
#             broadcast_msg_to_chat(msg, group_name=self.room_group_name, user='admin')
#             return True
#         return False
#
#
# def new_user_receiver(sender, instance, created, *args, **kargs):
#     if created:
#         # UserKlass = instance.__class__
#         # my_admin_user = UserKlass.objects.get(id=1)
#         # obj, created = Thread.objects.get_or_new(my_admin_user, instance.username)
#         # obj.broadcast(msg='Hello and welcome')
#
#         sender_id = 1  # admin user, main sender
#         receiver_id = instance.id
#         trigger_welcome_message(sender_id, receiver_id)
#
#
# post_save.connect(new_user_receiver, sender=settings.AUTH_USER_MODEL)


class PrivateChatMsg(models.Model):
    chat = models.ForeignKey(PrivateChat, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    msg = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class GroupChatQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class GroupChatManager(models.Manager):
    def get_queryset(self):
        return GroupChatQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


class GroupChat(models.Model):
    group_name = models.CharField(max_length=50)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class GroupChatMsg(models.Model):
    group = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    msg = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
