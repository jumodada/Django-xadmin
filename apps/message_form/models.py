from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('名字',max_length=64)
    sex = models.CharField('性别', default='1', choices=(
        ('1', 'men'),
        ('0', 'women'),
    ))
    username = models.CharField('用户名', unique=True, max_length=64)