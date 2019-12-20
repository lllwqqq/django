#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/20 下午3:19
@Author:  Aroma
@File: blog_extras.py
@Software: PyCharm
"""
from django  import template
from ..models import Post,Category,Tag

register = template.Library()



@register.inclusion_tag(filename='blog/inclusions/_recent_post.html',takes_context=True)
def show_recent_posts(context,num=5):
    post_list = Post.objects.all().order_by('-create_time')[:num]
    return {
        'post_list': post_list
    }

@register.inclusion_tag(filename='blog/inclusions/_archives.html',takes_context=True)
def archives(context):
    archives = Post.objects.dates(field_name='create_time',kind='month',order='DESC')
    return {
        'archives': archives
    }

@register.inclusion_tag(filename='blog/inclusions/_categories.html',takes_context=True)
def categories(context):
    categories = Category.objects.all()
    return {
        'categories': categories
    }

@register.inclusion_tag(filename='blog/inclusions/_tags.html',takes_context=True)
def tags(context):
    tags = Tag.objects.all()
    return {
        'tags': tags
    }