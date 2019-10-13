from django.db import models

from category.models import Category


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    title_pic = models.CharField(max_length=120)
    content = models.TextField()
    share_num = models.IntegerField()
    article_id = models.IntegerField()
    location = models.CharField(max_length=50)
    post_type = models.IntegerField()
    category = models.ForeignKey(Category, related_name='category_posts', on_delete=models.CASCADE)
    # topic = models.ManyToManyField(Topic, related_name='topic_posts')
    public = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def post_image_upload(instance, filename):
    return 'images/{username}/posts/{img_name}'.format(username=instance.post.user.username, img_name=filename)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=post_image_upload, height_field='image_height', width_field='image_width')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
