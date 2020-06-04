from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=100, verbose_name='分类')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    def __str__(self):
        return self.name


class Tag(models.Model):
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    name = models.CharField(max_length=100, blank=True, verbose_name='标签')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    title = models.CharField(max_length=200, verbose_name="标题")
    excerpt = models.CharField(max_length=100, blank=True, verbose_name='摘要')
    body = models.TextField(verbose_name='正文')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')
    modified_time = models.DateTimeField(verbose_name='修改时间', default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
