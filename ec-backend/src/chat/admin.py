from django.contrib import admin

from .models import PrivateChat, PrivateChatMsg, GroupChat, GroupChatMsg, ChannelName


class PrivateChatMsgAdmin(admin.TabularInline):
    model = PrivateChatMsg


class PrivateChatAdmin(admin.ModelAdmin):
    inlines = [PrivateChatMsgAdmin]

    class Meta:
        model = PrivateChat


admin.site.register(PrivateChat, PrivateChatAdmin)


class GroupChatMsgAdmin(admin.TabularInline):
    model = GroupChatMsg


class GroupChatAdmin(admin.ModelAdmin):
    inlines = [GroupChatMsgAdmin]

    class Meta:
        model = GroupChat


admin.site.register(GroupChat, GroupChatAdmin)

admin.site.register(ChannelName)
