from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from ec.permissions import IsBindPhone
from .serializers import LikeDetailSerializer, CommentSerializer
from .models import LikeInfo, LIKE_STATUS, Post


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
