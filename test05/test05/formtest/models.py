from django.db import models


# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    sex = models.BooleanField(verbose_name='性别', max_length=1, choices=((0, '男'), (1, '女'),), default=0)
    school = models.CharField(max_length=100, verbose_name='学校')
    addr = models.CharField(max_length=200, verbose_name='住址')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
