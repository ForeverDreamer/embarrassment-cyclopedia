from rest_framework import serializers

from .models import Category, Topic, Post, PostImage, PostVideo, POST_TYPE
from .validators import validate_file_type


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
            'id',
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


class TopicPostSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = [
            'title',
        ]

    def get_title(self, obj):
        return obj.title


class PostImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']


class PostVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostVideo
        fields = ['video']


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    nickname = serializers.CharField(source='user.profile.nickname', read_only=True)
    title = serializers.SerializerMethodField()
    category = serializers.CharField(source='category.title', read_only=True)
    topic = TopicPostSerializer(many=True)
    # postimage_set = PostImageSerializer(many=True, read_only=True)
    # postvideo_set = PostVideoSerializer(many=True, read_only=True)

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
            'topic',
            'like',
            'unlike',
            'share',
        ]
        extra_kwargs = {
            'url': {'view_name': 'content:post-detail'},
        }

    def get_title(self, obj):
        return obj.title

    # def get_title_pic(self, obj):
    #     return self.postimage_set[0]

    # peError: 'RelatedManager' object is not subscriptable
    # def get_title_pic(self, obj):
    #     return obj.postimage_set[0]


class PostDetailSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.profile.nickname', read_only=True)
    category = serializers.CharField(source='category.title', read_only=True)
    title = serializers.SerializerMethodField()
    postimage_set = PostImageSerializer(many=True, read_only=True)
    postvideo_set = PostVideoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'nickname',
            'title',
            'location',
            'post_type',
            'share_post',
            'category',
            'postimage_set',
            'postvideo_set',
        ]

    def get_title(self, obj):
        return obj.title


class PostCreateSerializer(serializers.ModelSerializer):
    topic = serializers.ListField(child=serializers.IntegerField())

    class Meta:
        model = Post
        fields = [
            # 'id',
            'desc',
            'location',
            'category',
            'topic',
            'post_type',
            'share_post',
            'public',
        ]
        # read_only_fields = ['id']

    def validate(self, data):
        if data['post_type'] == POST_TYPE[2][0] and len(data['share_post']) == 0:
            raise serializers.ValidationError("分享文章id缺失")
        data['share_post'] = []
        return data

    # def validate_category(self, category):
    #     # for slug, _ in CATEGORY_CHOICES:
    #     #     if category == slug:
    #     #         return category
    #     # qs = Category.objects.filter(id=category_id)
    #     # if qs.exists():
    #     #     return ca
    #     print(category)
    #     raise serializers.ValidationError('类别不存在！')

    # def create(self, validated_data):
    #     share_post = validated_data.get('share_post')
    #     if share_post:
    #         validated_data['active'] = True
    #     post = Post.objects.create(**validated_data)
    #     return post


class PostImageSerializer(serializers.Serializer):
    # post = PostCreateSerializer()
    post_id = serializers.CharField(max_length=20)
    file_list = serializers.ListField(child=serializers.ImageField())

    # class Meta:
    #     model = PostImage
    #     fields = ['post', 'image']

    def create(self, validated_data):
        image_list = validated_data.get('file_list')
        post = self.context.get('post')
        # post_data = validated_data.pop('post')
        print(self.context.get('post'))
        # post = Post.objects.create(**post_data)
        image_urls = []
        for image in image_list:
            post_img = PostImage.objects.create(post=post, image=image)
            image_urls.append(str(post_img))
        return image_urls


class PostVideoSerializer(serializers.Serializer):
    post_id = serializers.CharField(max_length=20)
    file_list = serializers.ListField(child=serializers.FileField(validators=[validate_file_type]))

    # def validate_file_type(upload):
    #     # Make uploaded file accessible for analysis by saving in tmp
    #     tmp_path = '{tmp_dir}/{filename}'.format(tmp_dir=TEMP_DIR, filename=upload.name[2:])
    #     default_storage.save(tmp_path, ContentFile(upload.file.read()))
    #     full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
    #     # Get MIME type of file using python-magic and then delete
    #     file_type = magic.from_file(full_tmp_path, mime=True)
    #     default_storage.delete(tmp_path)
    #     # Raise validation error if uploaded file is not an acceptable form of media
    #     if file_type not in settings.IMAGE_TYPES and file_type not in settings.VIDEO_TYPES:
    #         raise serializers.ValidationError('File type not supported. JPEG, PNG, or MP4 recommended.')

    def create(self, validated_data):
        video_list = validated_data.get('file_list')
        post = self.context.get('post')
        video_urls = []
        for video in video_list:
            post_video = PostVideo.objects.create(post=post, video=video)
            video_urls.append(str(post_video))
        return video_urls
