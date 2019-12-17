from rest_framework import serializers

from .models import AdInfo


class AdInfoListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdInfo
        fields = [
            'id',
            'url',
            'location',
            'link_url',
            'image',
        ]
        extra_kwargs = {
            'url': {'view_name': 'ad:adinfo-detail'},
        }


class AdInfoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdInfo
        fields = [
            'id',
            'location',
            'link_url',
            'image',
        ]
