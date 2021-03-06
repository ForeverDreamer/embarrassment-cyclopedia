from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters

from ec.permissions import IsBindPhone, IsOwnerOrReadOnly
from .serializers import (
    LikeDetailSerializer,
    CommentSerializer,
    BlockUserDetailSerializer,
    FollowUserDetailSerializer,
    FollowListSerializer,
    FeedbackSerializer,
    AppUpdateSerializer,
)
from .models import LikeInfo, LIKE_STATUS, BlockUser, FollowUser, Feedback, AppUpdate

User = get_user_model()


class LikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]

    def post(self, *args, **kwargs):
        serializer = LikeDetailSerializer(data=self.request.data)
        if not serializer.is_valid(raise_exception=False):
            # print(serializer.errors)
            return Response({'error_code': '3000', "msg": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.validated_data
        post = data.get('post')
        req_status = data.get('status')
        # 顶踩信息是否存在
        qs = LikeInfo.objects.filter(user=self.request.user, post=data.get('post'))
        if qs.exists():
            like = qs.first()
            if like.status == LIKE_STATUS[0][0]:
                if req_status == LIKE_STATUS[1][0]:
                    post.like -= 1
                    post.unlike += 1
                elif req_status == LIKE_STATUS[2][0]:
                    post.like -= 1
            elif like.status == LIKE_STATUS[1][0]:
                if req_status == LIKE_STATUS[0][0]:
                    post.like += 1
                    post.unlike -= 1
                elif req_status == LIKE_STATUS[2][0]:
                    post.unlike -= 1
            else:
                if req_status == LIKE_STATUS[0][0]:
                    post.like += 1
                elif req_status == LIKE_STATUS[2][0]:
                    post.unlike += 1
            like.status = req_status
            like.save()
            post.save()
            return Response({'error_code': '10000', "msg": "状态修改成功", 'data': {'status': like.status}},
                            status=status.HTTP_200_OK)
        else:
            if req_status == LIKE_STATUS[0][0]:
                post.like += 1
            elif req_status == LIKE_STATUS[1][0]:
                post.unlike += 1
            else:
                return Response({'error_code': '10001', "msg": "操作错误，状态未创建！"},
                                status=status.HTTP_400_BAD_REQUEST)
            like = serializer.save(user=self.request.user, post=data.get('post'))
            post.save()
            return Response({'error_code': '10001', "msg": "状态创建成功", 'data': {'status': like.status}},
                            status=status.HTTP_201_CREATED)


class CommentAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# 加入/解除黑名单
class BlockUserAPIView(generics.CreateAPIView, mixins.DestroyModelMixin):
    queryset = BlockUser.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsBindPhone, IsOwnerOrReadOnly]
    serializer_class = BlockUserDetailSerializer

    def get_object(self):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        blocked = data.get('blocked')
        qs = self.get_queryset()
        qs = qs.filter(blocked=blocked)
        if not qs.exists():
            return None
        obj = qs.first()
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blocked = serializer.validated_data.get('blocked')
        if blocked == self.request.user:
            return Response({'error_code': '10001', "msg": "不能拉黑自己！"}, status=status.HTTP_400_BAD_REQUEST)
        qs = BlockUser.objects.filter(blocked=blocked)
        if qs.exists():
            return Response({'error_code': '10001', "msg": "您已拉黑过该用户！"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(owner=self.request.user)
        return Response({'error_code': '10001', "msg": "拉黑操作成功！"}, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({'error_code': '10001', "msg": "您未拉黑该用户！"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# 关注/取关用户
class FollowUserAPIView(generics.CreateAPIView, mixins.DestroyModelMixin):
    queryset = FollowUser.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsBindPhone, IsOwnerOrReadOnly]
    serializer_class = FollowUserDetailSerializer

    def get_object(self):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        followed = data.get('followed')
        qs = self.get_queryset()
        qs = qs.filter(followed=followed)
        if not qs.exists():
            return None
        obj = qs.first()
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        followed = serializer.validated_data.get('followed')
        if followed == self.request.user:
            return Response({'error_code': '10001', "msg": "不能关注自己！"}, status=status.HTTP_400_BAD_REQUEST)
        qs = FollowUser.objects.filter(owner=self.request.user, followed=followed)
        if qs.exists():
            return Response({'error_code': '10001', "msg": "您已关注过该用户！"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(owner=self.request.user)
        return Response({'error_code': '10001', "msg": "关注成功！"}, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({'error_code': '10001', "msg": "您未关注该用户！"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


# 互关列表
class FriendListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]
    serializer_class = FollowListSerializer

    def get_queryset(self):
        return FollowUser.objects.friends(self.request.user)


# 粉丝列表
class FansListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]
    serializer_class = FollowListSerializer

    def get_queryset(self):
        return FollowUser.objects.fans(self.request.user)


# 关注列表
class FollowListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]
    serializer_class = FollowListSerializer

    def get_queryset(self):
        return FollowUser.objects.follows(self.request.user)


# 用户反馈
class FeedBackAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]
    serializer_class = FeedbackSerializer

    def get_queryset(self):
        return Feedback.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, customer_service=User.objects.get(id=1))


# 检查App版本
class CheckUpdateAPIView(generics.RetrieveAPIView):
    queryset = AppUpdate.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsBindPhone]
    serializer_class = AppUpdateSerializer
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ["create_time"]

    def get_object(self):
        qs = self.get_queryset().order_by('-create_time')
        if qs.exists():
            return qs.first()
        return None

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
