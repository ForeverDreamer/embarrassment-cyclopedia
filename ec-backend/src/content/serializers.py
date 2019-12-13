from rest_framework import serializers

from .models import Category, Topic, Post, PostImage, PostVideo, CATEGORY_CHOICES


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
            'slug',
            'title',
        ]


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
    category = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Topic
        fields = [
            'url',
            'title',
            'desc',
            'category',
        ]
        extra_kwargs = {
            'url': {'view_name': 'content:topic-detail'},
        }


class TopicDetailSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    title = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = [
            'title',
            'desc',
            'category',
        ]

    def get_title(self, obj):
        return obj.title


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.SerializerMethodField()

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

    def get_title(self, obj):
        return obj.title


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


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'desc',
            'location',
            'category',
            'post_type',
        ]
        # read_only_fields = ['id']

    # def validate_category(self, category):
    #     # for slug, _ in CATEGORY_CHOICES:
    #     #     if category == slug:
    #     #         return category
    #     # qs = Category.objects.filter(id=category_id)
    #     # if qs.exists():
    #     #     return ca
    #     print(category)
    #     raise serializers.ValidationError('类别不存在！')


class PostImageSerializer(serializers.ModelSerializer):
    # post = PostCreateSerializer()

    class Meta:
        model = PostImage
        fields = ['image', 'post']

    # def create(self, validated_data):
    #     # post_data = validated_data.pop('post')
    #     print(self.context.get('post'))
    #     # post = Post.objects.create(**post_data)
    #     post_img = PostImage.objects.create(post=self.context.get('post'), **validated_data)
    #     return post_img


class PostVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVideo
        fields = ['post', 'video']
