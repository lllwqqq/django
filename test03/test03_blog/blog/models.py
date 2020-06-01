from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse
from django.utils.html import strip_tags
import markdown


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='标签', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    excerpt = models.CharField(max_length=200, verbose_name='摘要',blank=True)
    body = models.TextField(verbose_name='正文')
    create_time = models.DateField(verbose_name='创建时间', default=timezone.now)
    modified_time = models.DateField(verbose_name='修改时间')

    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(extensions={
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        })
        if not self.excerpt:
            self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
