# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市')
    desc = models.CharField(max_length=200, verbose_name=u'城市描述', null=True, blank=True)

    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'机构名称')
    desc = models.TextField(verbose_name=u'机构描述')
    address = models.CharField(max_length=200, verbose_name=u'机构地址')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    image = models.ImageField(upload_to='organization/image/%Y/%m', verbose_name=u'封面图')
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')

    city = models.ForeignKey(CityDict, verbose_name=u'所在城市', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'机构信息'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'教师名字')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.IntegerField(default=0, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'公司职位')
    points = models.CharField(max_length=50, verbose_name=u'课程特点')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏数')
    click_nums = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateField(default=timezone.now, verbose_name=u'添加时间')
    org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构', on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'教师'
        verbose_name_plural = verbose_name
