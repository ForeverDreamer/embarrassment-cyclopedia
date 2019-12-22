from django.contrib import admin

from .models import LikeInfo, Comment, BlockUser, FollowUser

admin.site.register(LikeInfo)
admin.site.register(Comment)
admin.site.register(BlockUser)
admin.site.register(FollowUser)
