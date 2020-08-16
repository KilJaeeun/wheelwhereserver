"""wheelwhere_server URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from user.views import userViewSet
from facility.views import commentViewSet, postViewSet

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = routers.DefaultRouter()
router.register('users', userViewSet)  # prefix = movies , viewset = MovieViewSet

router.register('posts', postViewSet)
router.register('comments', commentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^api-jwt-auth/$', obtain_jwt_token),  # JWT 토큰 획득
    url(r'^api-jwt-auth/refresh/$', refresh_jwt_token),  # JWT 토큰 갱신
    url(r'^api-jwt-auth/verify/$', verify_jwt_token),  # JWT 토큰 확인

]
