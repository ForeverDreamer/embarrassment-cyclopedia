import random

from django.conf import settings
from django.db import models
# from django.db.models.signals import post_save
from django.utils import timezone

from .validators import validate_mobile_phone
from ec import config
from ec.utils import get_filename_ext

User = settings.AUTH_USER_MODEL

GENDER_STATUS = (
    ('male ', '男'),
    ('female', '女'),
    ('secret', '保密'),
)

EMOTION_STATUS = (
    ('single ', '单身'),
    ('in_love', '热恋'),
    ('married', '已婚'),
    ('secret', '保密'),
)

CAREER_STATUS = (
    ('teacher ', '教师'),
    ('it', 'IT'),
    ('public_servant', '公务员'),
    ('secret', '保密'),
)

THIRD_PARTY_TYPE = (
    ('wechat', '微信'),
    ('microblog', '微博'),
    ('qq', 'QQ'),
    ('others', '其他'),
)


class ProfileQuerySet(models.query.QuerySet):
    pass


class ProfileManager(models.Manager):
    def get_queryset(self):
        return ProfileQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all()
        # return super(CourseManager, self).all()


def user_pic_upload(instance, filename):
    return 'images/{id}/user_pics/{pic_name}'.format(id=instance.owner.id, pic_name=filename)


class Profile(models.Model):
    owner = models.OneToOneField('auth.User', related_name='profile', on_delete=models.CASCADE, null=True)
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    user_pic = models.ImageField(upload_to=user_pic_upload, height_field='image_height', width_field='image_width',
                                 blank=True, null=True)
    # validators必须要配合ModelForm使用，后台手动操作就是通过ModelForm
    # .create()或.save()不生效：'https://stackoverflow.com/questions/40881708/django-model-validator-not-working-on-create'
    mobile_phone = models.CharField(max_length=50, validators=[validate_mobile_phone], blank=True, null=True)
    cteate_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # status = models.BooleanField(default=True)
    gender = models.CharField(max_length=50, choices=GENDER_STATUS, default='secret')
    age = models.IntegerField(blank=True, null=True)
    emotion = models.CharField(max_length=50, choices=EMOTION_STATUS, default='secret')
    career = models.CharField(max_length=50, choices=CAREER_STATUS, default='secret')
    birthday = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    hometown = models.CharField(max_length=50, blank=True, null=True)
    logout = models.BooleanField(default=False)  # 用户手动退出登录

    objects = ProfileManager()

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.mobile_phone or self.owner.email


# def user_created_receiver(sender, instance, created, *args, **kwargs):
#     print('user_created_receiver: ', created)
#     print(kwargs)
#     if created:
#         if not instance.is_staff:
#             Profile.objects.get_or_create(owner=instance, *args, **kwargs)
#
#
# post_save.connect(user_created_receiver, sender=User)


def third_user_pic_upload(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image/third_login/{openid}/{final_filename}".format(
        openid=instance.openid,
        final_filename=final_filename
    )


class ThirdLoginInfo(models.Model):
    owner = models.ForeignKey('auth.User', related_name='third_set', on_delete=models.CASCADE, blank=True, null=True)
    third_type = models.CharField(max_length=50, choices=THIRD_PARTY_TYPE, default='others')
    openid = models.CharField(max_length=200)
    nickname = models.CharField(max_length=50)
    logout = models.BooleanField(default=True)  # 用户手动退出登录
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    third_user_pic = models.ImageField(upload_to=third_user_pic_upload, height_field='image_height',
                                       width_field='image_width',
                                       blank=True, null=True)
    # expires_time = models.DateTimeField(default=(timezone.now() + 7200))

    class Meta:
        verbose_name = 'ThirdLoginInfo'
        verbose_name_plural = 'ThirdLoginInfos'

    def __str__(self):
        return '_'.join([self.nickname, self.third_type])
