from django.db import models


class User(models.Model):
    name = models.CharField(max_length=32, verbose_name='用户名')
    password = models.CharField(max_length=256, verbose_name='密码')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
