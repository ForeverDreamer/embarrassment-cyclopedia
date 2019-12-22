from django.contrib import admin

from .models import LikeInfo, Comment, BlockUser, FollowUser, Feedback, AppUpdate

admin.site.register(LikeInfo)
admin.site.register(Comment)
admin.site.register(BlockUser)
admin.site.register(FollowUser)
admin.site.register(Feedback)
admin.site.register(AppUpdate)
