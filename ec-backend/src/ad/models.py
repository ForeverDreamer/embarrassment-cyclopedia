import uuid

from django.db import models

from ec.utils import get_filename_ext

AD_LOCATION = (
    # 注意不要有空格，否则会出现各种乱七八糟的问题
    ('carousel', '动态轮播图'),
    ('personal_center', '个人中心'),
)


def ad_image_upload(instance, filename):
    new_filename = uuid.uuid4()
    name, ext = get_filename_ext(filename)
    image_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "image/ad/{location}/{image_name}".format(
        location=instance.location,
        image_name=image_name
    )


class AdInfo(models.Model):
    location = models.CharField(max_length=20, choices=AD_LOCATION)
    link_url = models.CharField(max_length=50)
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=ad_image_upload, height_field='image_height',
                              width_field='image_width',
                              blank=True, null=True)

    class Meta:
        verbose_name = 'AdInfo'
        verbose_name_plural = 'AdInfos'

    def __str__(self):
        return self.location
