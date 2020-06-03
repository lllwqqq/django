from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="标题")
    author = models.CharField(max_length=100)
    body = models.TextField()
    create_time = models.DateTimeField(default=datetime.now)
    modifiy_time = models.DateTimeField()

    excerpt = models.CharField(max_length=100, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
