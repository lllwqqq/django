# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'课程名字')
    desc = models.CharField(max_length=100, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(max_length=100, verbose_name=u'难度', choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')))
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name=u'封面图')
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Courses, verbose_name=u'课程', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u'章节')
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name


class CourseResource(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'资源名')
    download = models.FileField(upload_to='apps/courses/resource/%Y/%m', verbose_name=u'资源文件', max_length=100)
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')
    course = models.ForeignKey(Courses, verbose_name=u'课程名称', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name
