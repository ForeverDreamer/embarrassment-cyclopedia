from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="category:detail", lookup_field='slug')

    class Meta:
        model = Category
        fields = [
            'id',
            'url',
            'slug',
            'title',
        ]
