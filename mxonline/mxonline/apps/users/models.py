# _*_ coding:utf-8 _*_
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from django.db import models


# Create your models here.

class UserProfile(AbstractUser):
    nic_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
    birthday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')), default='female',
                              verbose_name=u'性别')
    address = models.CharField(max_length=500, verbose_name=u'地址', default='')
    mobile = models.CharField(verbose_name=u'电话', max_length=11)
    image = models.FileField(max_length=200, upload_to='image/%Y/%m', default=u'image/default.png', verbose_name=u'头像')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=50, verbose_name=u'验证码')
    email = models.EmailField(max_length=100, verbose_name=u'邮箱')
    send_type = models.CharField(max_length=50, choices=(('register', u'注册'), ('forget', u'找回密码')))
    send_time = models.DateField(verbose_name=u'发送时间', default=timezone.now)

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name=u'轮播图')
    index = models.IntegerField(default=100, verbose_name=u'顺序')
    url = models.URLField(max_length=200, verbose_name=u'访问地址')
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
