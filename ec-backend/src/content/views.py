from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Topic, Post, POST_TYPE
from ec.permissions import IsBindPhone, IsOwnerOrReadOnly
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


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


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


class PostUploadFileView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]
    parser_class = (FileUploadParser,)

    def post(self, *args, **kwargs):
        post_type = self.request.data.get('post_type')
        if post_type == POST_TYPE[0][0]:
            file_serializer = PostImageSerializer(data=self.request.data)
        elif post_type == POST_TYPE[1][0]:
            file_serializer = PostVideoSerializer(data=self.request.data)
        else:
            return Response({'msg': 'post_type错误'}, status=status.HTTP_400_BAD_REQUEST)
        if not file_serializer.is_valid():
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        post_id = file_serializer.validated_data.get('post_id')
        qs = Post.objects.filter(id=post_id)
        if not qs.exists():
            return Response({'msg': 'post未创建'}, status=status.HTTP_400_BAD_REQUEST)
        post = qs.first()
        if not self.request.user == post.user:
            return Response({'msg': '用户不一致'}, status=status.HTTP_400_BAD_REQUEST)
        if not post_type == post.post_type:
            return Response({'msg': 'post_type不一致'}, status=status.HTTP_400_BAD_REQUEST)
        file_serializer.context['post'] = qs.first()
        file_urls = file_serializer.save()
        post.active = True
        post.title_pic = file_urls[0]
        post.save()
        return Response({'msg': '文件上传成功!', 'file_urls': file_urls}, status=status.HTTP_201_CREATED)

#
# class PostUploadVideoView(APIView):
#     permission_classes = [permissions.IsAuthenticated, IsBindPhone]
#     parser_class = (FileUploadParser,)
#
#     def post(self, request, *args, **kwargs):
#         video_serializer = PostVideoSerializer(data=request.data)
#         if not video_serializer.is_valid():
#             return Response(video_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         video_serializer.save()
#         return Response({'msg': '视频上传成功!'}, status=status.HTTP_201_CREATED)
