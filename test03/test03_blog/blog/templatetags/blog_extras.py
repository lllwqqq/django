#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/6 下午7:01
@Author:  Aroma
@File: blog_extras.py
@Software: PyCharm
"""

from django import template

from ..models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag(filename='blog/extras/_show_recent_post.html', takes_context=True)
def show_recent_posts(context, num=5):
    post = Post.objects.all().order_by('-create_time')[:num]
    return {
        'recent_post_list': post
    }

@register.inclusion_tag(filename='blog/extras/_archives.html',takes_context=True)
def archives(context,):
    archives = Post.objects.dates('create_time',kind='month',order='DESC')
    return {
        'archives': archives
    }

@register.inclusion_tag(filename='blog/extras/_categories.html',takes_context=True)
def categories(context):
    categories = Category.objects.all()
    return {
        'categories': categories
    }

@register.inclusion_tag(filename='blog/extras/_tags.html',takes_context=True)
def tags(context):
    tags = Tag.objects.all()
    return {
        'tags' : tags
    }
