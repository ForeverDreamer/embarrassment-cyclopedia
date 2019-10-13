from rest_framework import generics, permissions

from .models import Topic
from .serializers import TopicSerializer


class TopicListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    # queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_queryset(self):
        sub = self.request.query_params.get('q')
        qs = Topic.objects.sub_category(sub)
        return qs


class TopicDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
