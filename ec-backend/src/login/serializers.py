from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Profile, ThirdLoginInfo
from .utils import is_phone, is_veri_code, validate_password, validate_third_type
from ec import config


class ThirdBindPhoneSerializer(serializers.Serializer):
    openid = serializers.CharField(max_length=100)
    mobile_phone = serializers.CharField(max_length=50)
    veri_code = serializers.CharField(max_length=20)

    def validate_mobile_phone(self, mobile_phone):
        if not is_phone(mobile_phone):
            raise serializers.ValidationError('请输入正确的电话号码！')
        return mobile_phone

    def validate_veri_code(self, veri_code):
        if not is_veri_code(veri_code):
            raise serializers.ValidationError('验证码格式错误！')
        return veri_code


class ThirdLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThirdLoginInfo
        fields = ['third_type', 'openid', 'nickname', 'third_user_pic']

    def create(self, validated_data):
        # 获取临时用户
        tmp_user, created = User.objects.get_or_create(username=config.TEMP_USER_INFO.get('username'),
                                                       password=config.TEMP_USER_INFO.get('password'))
        # 创建第三方登录信息
        ThirdLoginInfo.objects.create(owner=tmp_user, **validated_data)
        return tmp_user


class CodeRegOrLoginSerializer(serializers.Serializer):
    mobile_phone = serializers.CharField()
    veri_code = serializers.CharField()

    def validate_mobile_phone(self, mobile_phone):
        if not is_phone(mobile_phone):
            raise serializers.ValidationError('手机号格式错误！')
        return mobile_phone

    def validate_veri_code(self, veri_code):
        if not is_veri_code(veri_code):
            raise serializers.ValidationError('验证码格式错误！')
        return veri_code

    def create(self, validated_data):
        mobile_phone = validated_data.get('mobile_phone')
        # 创建用户
        user = User.objects.create_user(username=mobile_phone, password=config.DEFALT_PASSWORD)
        # 创建用户信息
        Profile.objects.create(owner=user, mobile_phone=mobile_phone)
        return user

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     return instance


class EmailRegSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    # def validate_mobile_phone(self, mobile_phone):
    #     if not is_phone(mobile_phone):
    #         raise ValidationError('validate_mobile_phone: 请输入正确的电话号码！')
    #     return mobile_phone

    def validate_password(self, password):
        if not validate_password(password):
            raise serializers.ValidationError('validate_veri_code: 密码格式错误！')
        return password

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')

        # 创建用户
        user = User.objects.create_user(username='user_' + email, email=email, password=password)
        # 创建用户信息
        Profile.objects.create(owner=user)
        return user


class AccountLoginSerializer(serializers.Serializer):
    mobile_phone = serializers.CharField(required=False, max_length=20)
    email = serializers.EmailField(required=False)
    password = serializers.CharField(max_length=50)

    def validate_mobile_phone(self, mobile_phone):
        if not is_phone(mobile_phone):
            raise serializers.ValidationError('请输入正确的电话号码！')
        return mobile_phone

    # def validate_email(self, email):
    #     if not is_phone(email):
    #         raise serializers.ValidationError('validate_mobile_phone: 请输入正确的电话号码！')
    #     return email

    def validate_password(self, password):
        if not validate_password(password):
            raise serializers.ValidationError('密码格式错误！')
        return password


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Profile
        fields = ['id', 'url', 'owner', 'mobile_phone', 'gender', 'age', 'emotion', 'career', 'birthday', 'hometown']


# class CodeRegOrLoginSerializer(serializers.ModelSerializer):
#     mobile_phone = serializers.CharField()
#     # veri_code = serializers.CharField()  # 该字段不属于Profile，不能够在这里验证
#
#     class Meta:
#         model = Profile
#         fields = ['mobile_phone']
#         # fields = ['mobile_phone', 'veri_code']
#
#     def validate_mobile_phone(self, mobile_phone):
#         if not is_phone(mobile_phone):
#             raise ValidationError('validate_mobile_phone: 请输入正确的电话号码！')
#         return mobile_phone
#
#     # def validate_veri_code(self, veri_code):
#     #     if not is_veri_code(veri_code):
#     #         raise ValidationError('validate_veri_code: 验证码格式错误！')
#     #     return veri_code
#
#     def create(self, validated_data):
#         # 创建用户信息
#         mobile_phone = validated_data.get('mobile_phone')
#         profile = Profile.objects.create(mobile_phone=mobile_phone)
#         # 创建用户
#         user = User.objects.create_user('user_' + mobile_phone)
#         profile.owner = user
#         profile.save()
#         return profile


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
