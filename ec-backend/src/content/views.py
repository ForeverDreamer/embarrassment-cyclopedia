from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Topic, Post
from .permissions import IsBindPhone
from .serializers import (
    CategoryListSerializer,
    CategoryDetailSerializer,
    TopicListSerializer,
    TopicDetailSerializer,
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    PostImageSerializer,
    PostVideoSerializer,
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    # def get_queryset(self):
    #     print(self.request.user)
    #     return Category.objects.all()


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'


class TopicListView(generics.ListAPIView):
    # permission_classes = [permissions.AllowAny]
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer

    def get_queryset(self):
        category = self.request.query_params.get('q')
        qs = Topic.objects.by_category(category)
        return qs


class TopicDetailView(generics.RetrieveAPIView):
    # permission_classes = [permissions.AllowAny]
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
    # lookup_field = 'slug'


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    def create(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        post = serializer.save(user=self.request.user)
        return Response({'error_code': '10002', "msg": "手机验证码注册成功", 'data': {'post_id': post.id}},
                        status=status.HTTP_201_CREATED)


class PostUploadImageView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]
    parser_class = (FileUploadParser,)

    def post(self, *args, **kwargs):
        img_serializer = PostImageSerializer(data=self.request.data)
        if not img_serializer.is_valid():
            return Response(img_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        img_serializer.save()
        # qs = Post.objects.filter(id=post_data.get('id'))
        # if qs.exists():
        #     post = qs.first()
        # else:
        #     post = Post.objects.create(user=self.request.user, post_type='image', **post_data)
        # serializer.save(context={'post': post})
        return Response({'msg': '图片上传成功!'}, status=status.HTTP_201_CREATED)
        #
        # if image_serializer.is_valid():
        #     image_serializer.save()
        #     return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # post_id = request.data.get('post')
        # images = request.data.get('images')
        # for _, img in images:
        #     data = {
        #         'post': post_id,
        #         'image': img
        #     }
        #     file_serializer = PostImageSerializer(data=data)
        #
        #     if file_serializer.is_valid():
        #         file_serializer.save()
        #     else:
        #         return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'msg': '图片上传成功！'}, status=status.HTTP_201_CREATED)


class PostUploadVideoView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        video_serializer = PostVideoSerializer(data=request.data)
        if not video_serializer.is_valid():
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        video_serializer.save()
        return Response({'msg': '视频上传成功!'}, status=status.HTTP_201_CREATED)
