from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import LikeInfo, Comment, BlockUser, FollowUser, Feedback, AppUpdate

User = get_user_model()


class FollowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username'
        ]


class FollowUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUser
        fields = [
            'followed',
        ]


class BlockUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlockUser
        fields = [
            'blocked',
        ]


class LikeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeInfo
        fields = [
            'post',
            'status',
        ]


# class LikeApiSerializer(serializers.Serializer):
#     action = serializers.CharField(max_length=20)
#     like_detail = LikeDetailSerializer()
#
#     def validate_action(self, action):
#         if action not in LIKE_STATUS:
#             raise serializers.ValidationError('操作错误！')
#         return action


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'post',
            'parent',
            'text',
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = [
            'question'
        ]


class AppUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUpdate
        fields = [
            'url',
            'version'
        ]
