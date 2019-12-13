from rest_framework import serializers

from .models import Category, Topic, Post, PostImage, PostVideo


class CategoryListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'url',
            'title',
        ]
        extra_kwargs = {
            'url': {'view_name': 'content:category-detail', 'lookup_field': 'slug'},
        }


class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'url',
            'slug',
            'title',
        ]
        extra_kwargs = {
            'url': {'view_name': 'content:category-detail', 'lookup_field': 'slug'},
        }


# class CategorySerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="category:detail", lookup_field='slug')
#
#     class Meta:
#         model = Category
#         fields = [
#             'id',
#             'url',
#             'slug',
#             'title',
#         ]


class TopicListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic
        fields = [
            'title',
            'desc',
        ]


class TopicDetailSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Topic
        fields = [
            'id',
            'title',
            'category',
            'desc',
        ]
        extra_kwargs = {
            'url': {'view_name': 'content:topic-detail', 'lookup_field': 'slug'},
        }


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'url',
            'nickname',
            'title',
            'title_pic',
            'location',
            'post_type',
            'category',
        ]


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    nickname = serializers.CharField(source='user.profile.nickname', read_only=True)

    class Meta:
        model = Post
        fields = [
            'nickname',
            'title',
            'title_pic',
            'location',
            'post_type',
            'category',
            'article',
            'postimage_set',
            'postvideo_set',
        ]


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['post', 'image']


class PostVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = ['post', 'video']
