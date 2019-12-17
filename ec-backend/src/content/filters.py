from django_filters import FilterSet, CharFilter

from .models import Post, Topic


class TopicFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains', distinct=True)

    class Meta:
        model = Topic
        fields = [
            'title',
        ]


class PostFilter(FilterSet):
    post_type = CharFilter(field_name='post_type', lookup_expr='iexact', distinct=True)

    class Meta:
        model = Post
        fields = [
            'post_type',
        ]
