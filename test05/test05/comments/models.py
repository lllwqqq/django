from django.db import models
from django.utils import timezone
from blog.models import Post


# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱', max_length=100)
    url = models.CharField(max_length=100, verbose_name='网址')
    text = models.TextField(verbose_name='评论')

    create_time = models.DateField(verbose_name='创建时间', default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,verbose_name='文章')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])

