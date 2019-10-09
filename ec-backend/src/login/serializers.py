from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .models import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = ['id', 'url', 'owner', 'mobile_phone', 'gender', 'age', 'emotion', 'career', 'birthday', 'hometown']


class UserCodeLoginSerializer(serializers.ModelSerializer):
    veri_code = serializers.CharField()

    class Meta:
        model = Profile
        fields = ['mobile_phone', 'veri_code']

    def create(self, validated_data):
        # 创建用户信息
        mobile_phone = validated_data.get('mobile_phone')
        profile = Profile.objects.create(mobile_phone=mobile_phone)
        # 创建用户
        user = User.objects.create_user('user_' + mobile_phone)
        profile.owner = user
        profile.save()
        return user


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # profile_url = serializers.HyperlinkedRelatedField(view_name='profile-detail', read_only=True)
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'profile']
        # fields = ['id', 'url', 'username', 'email', 'password', 'profile', 'profile_url']
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(owner=user, **profile_data)
        return user

    # def update(self, instance, validated_data):
    #     validated_data.pop('password')
    #     instance.save(**validated_data, partial=True)
    #     return instance
