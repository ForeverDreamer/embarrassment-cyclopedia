from django.contrib import admin

from .models import Category, Topic, Post, PostImage, PostVideo

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostVideo)
