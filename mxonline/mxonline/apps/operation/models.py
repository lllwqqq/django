# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from users.models import UserProfile
from courses.models import Courses


# Create your models here.


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    phone = models.CharField(max_length=11, verbose_name=u'联系电话')
    course = models.CharField(max_length=50, verbose_name=u'课程名称')
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户咨询'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, verbose_name=u'课程', on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name=u'评论内容')
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程评论'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '{0}:{1}'.format(self.user,self.course)


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户')
    fav_id = models.IntegerField(default=0, verbose_name=u'数据id')
    fav_type = models.IntegerField(choices=(('1', '课程'), ('2', '课程机构'), ('3', '讲师')), default=1, verbose_name=u'收藏类型')
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name=u'用户')
    message = models.CharField(max_length=300, verbose_name=u'消息')
    has_read = models.BooleanField(default=False, verbose_name=u'是否已读')
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户消息'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u'用户', on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, verbose_name=u'课程', on_delete=models.CASCADE)
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'用户课程'
        verbose_name_plural = verbose_name
