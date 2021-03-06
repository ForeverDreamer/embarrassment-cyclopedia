import uuid

from django.db import models

from ec.utils import get_filename_ext


POST_TYPE = (
    ('image', '图文'),
    ('video', '视频'),
    ('share', '分享转发'),
)

CATEGORY_CHOICES = (
    ('follow', '关注'),
    ('recommends', '推荐'),
    ('sports', '体育'),
    ('hot', '热点'),
    ('finance', '财经'),
    ('entertainment', '娱乐'),
)


class CategoryQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, choices=CATEGORY_CHOICES)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CategoryManager()

    def __str__(self):
        return self.title


class TopicQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    # def by_category(self, sub):
    #     qs = self.filter(category__slug=sub)
    #     return qs


class TopicManager(models.Manager):
    def get_queryset(self):
        return TopicQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    # def by_category(self, category):
    #     if category:
    #         return self.all().by_category(category)
    #     else:
    #         return self.all()


class Topic(models.Model):
    title = models.CharField(max_length=120)
    title_pic = models.CharField(max_length=120)
    # slug = models.SlugField(unique=True)
    desc = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TopicManager()

    def __str__(self):
        return self.title


class PostQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def public(self):
        return self.filter(public=True)

    def by_user(self, user):
        qs = self.filter(user=user)
        return qs

    def by_topic(self, topic):
        qs = self.filter(topic__title__icontains=topic)
        return qs.distinct()


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active().public()

    def by_user(self, user):
        return self.get_queryset().active().by_user(user)

    def by_topic(self, topic):
        qs = self.get_queryset().active().by_topic(topic)
        return qs


class Post(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # title = models.CharField(max_length=120)
    desc = models.TextField()
    title_pic = models.CharField(max_length=120, null=True, blank=True)
    # article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=50)
    post_type = models.CharField(max_length=10, choices=POST_TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topic, blank=True)
    public = models.BooleanField(default=True)
    like = models.IntegerField(default=0)
    unlike = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    share_post = models.ManyToManyField('self', blank=True)
    active = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    # def __str__(self):
    #     return self.id

    @property
    def title(self):
        return self.desc[:10]

    # TypeError: 'RelatedManager' object is not subscriptable
    # @property
    # def title_pic(self):
    #     return self.postimage_set[0]


def post_image_upload(instance, filename):
    # new_filename = random.randint(1111111111, 9999999999)
    new_filename = uuid.uuid4()
    name, ext = get_filename_ext(filename)
    img_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    # return 'image/post/{img_name}'.format(img_name=img_name)
    return 'image/post/{post_id}/{img_name}'.format(post_id=instance.post.id, img_name=img_name)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=post_image_upload, height_field='image_height', width_field='image_width')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.image)


def post_video_upload(instance, filename):
    new_filename = uuid.uuid4()
    name, ext = get_filename_ext(filename)
    video_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return 'video/post/{post_id}/{video_name}'.format(post_id=instance.post.id, video_name=video_name)


class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to=post_video_upload)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.video)
