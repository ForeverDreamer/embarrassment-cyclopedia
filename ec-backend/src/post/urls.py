from django.urls import path

from .views import PostImageUploadView

urlpatterns = [
    path('upload/', PostImageUploadView.as_view(), name='upload'),
]
