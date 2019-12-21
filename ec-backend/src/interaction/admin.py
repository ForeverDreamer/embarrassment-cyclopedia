from django.contrib import admin

from .models import LikeInfo, Comment, BlockUser

admin.site.register(LikeInfo)
admin.site.register(Comment)
admin.site.register(BlockUser)
