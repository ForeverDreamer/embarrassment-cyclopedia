from django.urls import path

from .views import (
    AdInfoListView,
    AdInfoDetailView,
    )

urlpatterns = [
    path('', AdInfoListView.as_view(), name='adinfo-list'),
    path('<str:pk>/', AdInfoDetailView.as_view(), name='adinfo-detail'),
]
