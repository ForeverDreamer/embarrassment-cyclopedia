from rest_framework import generics

from .models import AdInfo
from .serializers import AdInfoListSerializer, AdInfoDetailSerializer


class AdInfoListView(generics.ListAPIView):
    queryset = AdInfo.objects.all()
    serializer_class = AdInfoListSerializer


class AdInfoDetailView(generics.RetrieveAPIView):
    queryset = AdInfo.objects.all()
    serializer_class = AdInfoDetailSerializer
