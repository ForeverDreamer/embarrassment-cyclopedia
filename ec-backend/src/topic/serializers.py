from rest_framework import serializers

from .models import Topic


class TopicSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)

    class Meta:
        model = Topic
        fields = [
            'id',
            'title',
            'category',
            'desc',
        ]
