from rest_framework import serializers
from viodes.models import *


# 序列化器
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'sex', 'email', 'create_time')


class ImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = ('src', 'title', 'summary', 'flag', 'create_time')


class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('src', 'title', 'summary', 'flag', 'create_time')


class CategoryVidSerializers(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('nid', 'title', 'video')


class CategoryImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('nid', 'title', 'Img')
