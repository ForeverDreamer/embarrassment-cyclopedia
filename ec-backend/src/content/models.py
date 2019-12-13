import random

from django.db import models

from ec.utils import get_filename_ext

POST_TYPE = (
    ('image ', '图文'),
    ('video', '视频'),
)


class CategoryQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().active()


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CategoryManager()

    def __str__(self):
        return self.title


class TopicQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def sub_category(self, sub):
        qs = self.filter(category__slug=sub)
        return qs


class TopicManager(models.Manager):
    def get_queryset(self):
        return TopicQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().active()

    def sub_category(self, sub):
        if sub:
            return self.all().sub_category(sub)
        else:
            return self.all()


class Topic(models.Model):
    title = models.CharField(max_length=120)
    title_pic = models.CharField(max_length=120)
    # slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.CharField(max_length=120)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TopicManager()

    def __str__(self):
        return self.title


class ArticleQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class ArticleManager(models.Manager):
    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().active()


class Article(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ArticleManager()

    def __str__(self):
        return self.title


class PostQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().active()


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    title_pic = models.CharField(max_length=120)
    desc = models.TextField()
    share_num = models.IntegerField()
    article = models.ForeignKey(Article, null=True, blank=True, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    post_type = models.CharField(max_length=10, choices=POST_TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # topic = models.ManyToManyField(Topic, related_name='topic_posts')
    public = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    def __str__(self):
        return self.title


def post_image_upload(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    img_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return 'image/{username}/posts/{img_name}'.format(username=instance.post.user.username, img_name=img_name)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=post_image_upload, height_field='image_height', width_field='image_width')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name


def post_video_upload(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    video_name = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return 'video/post/{username}/{video_name}'.format(username=instance.post.user.username, video_name=video_name)


class PostVideo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    video = models.FileField(upload_to=post_video_upload)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
