from rest_framework import serializers
from .models import user


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user  # 모델 설정
        fields = ('id', 'name', 'cell_phone', 'password', 'email')  # 필드 설정
