from django.contrib import admin

from .models import Category, Topic, Post, PostImage

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(PostImage)
