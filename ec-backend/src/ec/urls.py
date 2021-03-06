"""ec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.staticfiles.views import serve

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from account import views

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('favicon.ico', serve, {'path': 'image/favicon.ico'}),
    path('admin/', admin.site.urls),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('account/', include(('account.urls', 'account'), namespace='account')),
    path('content/', include(('content.urls', 'content'), namespace='content')),
    path('ad/', include(('ad.urls', 'ad'), namespace='ad')),
    path('interaction/', include(('interaction.urls', 'interaction'), namespace='interaction')),
    path('chat/', include(('chat.urls', 'chat'), namespace='chat')),
    # re_path(r'^api/auth/$', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
