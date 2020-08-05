from rest_framework import serializers

from .models import *


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post  # 모델 설정
        fields = ('id', 'name', 'description', 'latitude', 'longitude', 'star', 'author')  # 필드 설정


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment  # 모델 설정
        fields = ('id', 'post', 'text', 'star', 'author')  # 필드 설정
