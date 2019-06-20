from django.db import models

# Create your models here.
type = (
    ('1', 'github'),
    ('2', 'qq'),
    ('3', 'weibo')
)


class User(models.Model):
    gender = (
        ('man', '男'),
        ('wman', '女')
    )
    username = models.CharField(max_length=32)  # 用户名
    password = models.CharField(max_length=32)  # 用户密码

    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    signature = models.CharField(max_length=64)
    is_active = models.BooleanField()
    download_image = models.ImageField(upload_to='static/images')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)


class OAuth_ex(models.Model):
    user = models.ForeignKey(User)
    openid = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=1, choices=type)
