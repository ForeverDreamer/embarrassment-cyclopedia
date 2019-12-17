from django.test import TestCase
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework.test import APIClient, RequestsClient, APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from account.models import Profile
from content.models import Category, CATEGORY_CHOICES
from ec import config
from account.utils import get_tokens_for_user
# from ..views import PostCreateView


class PostViewTestCase(APITestCase):
    def setUp(self):
        """每次运行测试示例都会重新创建默认数据库，不会使用db.sqlite，所以数据也必须重新写入"""
        self.username = '18623370060'
        self.password = config.DEFALT_PASSWORD
        # 创建用户
        user = User.objects.create_user(username=self.username, password=self.password)
        # 创建用户信息
        Profile.objects.create(owner=user, mobile_phone=self.username)
        self.token = 'Bearer ' + get_tokens_for_user(user)['access']
        self.client.credentials(HTTP_AUTHORIZATION=self.token)
        # 初始化分类数据
        for slug, title in CATEGORY_CHOICES:
            Category.objects.create(slug=slug, title=title)
        # 初始化话题数据

    def test_categorylist_views(self):
        response = self.client.get('/content/category/')
        # print(type(response.data))
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for dic in response.data:
            # print(dic)
            self.assertIn('url', dic.keys())
            self.assertIn('title', dic.keys())

    def test_postlist_views(self):
        # self.client.headers.update({'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoi'
        #                                              'YWNjZXNzIiwiZXhwIjoxNTc2NTUzODI4LCJqdGkiOiIyMjM2ZjQ0MzU3MTA0YTVk'
        #                                              'ODBkZGZhMTYyZjNhZGRkZiIsInVzZXJfaWQiOjN9.qf6WF-8iOYaDQ7pbS_LfJVE'
        #                                              'y4ZH67FAih0wxnGiLahY'})
        # self.client.login(username='18623370060', password='8ui#twrb01&6')
        # self.client.credentials(
        #     HTTP_AUTHORIZATION='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTc2NTUzODI4LCJqdGkiOiIyMjM2ZjQ0MzU3MTA0YTVkODBkZGZhMTYyZjNhZGRkZiIsInVzZXJfaWQiOjN9.qf6WF-8iOYaDQ7pbS_LfJVEy4ZH67FAih0wxnGiLahY')
        # response = self.client.get(settings.BASE_URL + api_reverse('content:category-list'), headers={'Authorization': TOKEN})
        response = self.client.get('/content/post/')
        # response = self.client.get(settings.BASE_URL)
        # print(settings.BASE_URL + api_reverse('content:category-list'))
        # print(response.status_code)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_postcreate_views(self):
    #     response = self.client.post(api_reverse('content:post-create'))