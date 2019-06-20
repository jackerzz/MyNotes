import uuid

from django.db import models


class User(models.Model):
    gender = (
        ('man', '男'),
        ('wman', '女')
    )
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 用户密码
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username


class Img(models.Model):
    flag = (
        (1, '正常'),
        (0, '删除')
    )
    src = models.ImageField(max_length=32, verbose_name='图片路径', upload_to='images/')
    title = models.CharField(max_length=16, verbose_name='标题')
    summary = models.CharField(max_length=128, verbose_name='简介')
    flag = models.IntegerField(verbose_name='标记图片状态', choices=flag)  # 0 和 1 用于伪删除
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '图片'

    def __str__(self):
        return self.title


class Videos(models.Model):
    flag = (
        (1, '正常'),
        (0, '删除')
    )
    src = models.FileField(max_length=32, verbose_name='视频路径', upload_to='Video/')
    title = models.CharField(max_length=16, verbose_name='标题')
    summary = models.CharField(max_length=128, verbose_name='简介')
    flag = models.IntegerField(verbose_name='标记图片状态', choices=flag)  # 0 和 1 用于伪删除
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = '视频'

    def __str__(self):
        return self.title


# 处理后的图片存放位置
class AutoVideoFile(models.Model):

    ogg_480_file = models.FileField(verbose_name='480图片路径',upload_to='Videos/TranscodingVideo/P480')
    wav_360_file = models.FileField(verbose_name='360图片路径',upload_to='Videos/TranscodingVideo/P360')
    mkv_720_file = models.FileField(verbose_name='720图片路径',upload_to='Videos/TranscodingVideo/P720')

    class Meta:
        verbose_name_plural = '转码后的视频'


class CategoryVid(models.Model):
    """
    视频分类
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=32)
    video = models.ForeignKey(verbose_name='所属用户', to='User', to_field='id')

    class Meta:
        verbose_name_plural = '视频分类'


class CategoryImg(models.Model):
    """
    图片分类
    """
    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='分类标题', max_length=32)
    Img = models.ForeignKey(verbose_name='所属用户', to='User', to_field='id')

    class Meta:
        verbose_name_plural = '图片分类'
