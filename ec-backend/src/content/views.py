from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Topic, Post
from .serializers import (
    CategoryListSerializer,
    CategoryDetailSerializer,
    TopicListSerializer,
    TopicDetailSerializer,
    PostListSerializer,
    PostDetailSerializer,
    PostImageSerializer,
    PostVideoSerializer,
)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    lookup_field = 'slug'


class TopicListView(generics.ListAPIView):
    # permission_classes = [permissions.AllowAny]
    queryset = Topic.objects.all()
    serializer_class = TopicListSerializer

    # def get_queryset(self):
    #     sub = self.request.query_params.get('q')
    #     qs = Topic.objects.sub_category(sub)
    #     return qs


class TopicDetailView(generics.RetrieveAPIView):
    # permission_classes = [permissions.AllowAny]
    queryset = Topic.objects.all()
    serializer_class = TopicDetailSerializer
    lookup_field = 'slug'


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class PostUploadImageView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        image_serializer = PostImageSerializer(data=request.data)

        if image_serializer.is_valid():
            image_serializer.save()
            return Response(image_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

        if video_serializer.is_valid():
            video_serializer.save()
            return Response(video_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)