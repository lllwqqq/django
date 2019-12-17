#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/17 下午4:03
@Author:  Aroma
@File: blog_extras.py
@Software: PyCharm
"""
from django import template
from ..models import Category,Tag,Post

register = template.Library()


@register.inclusion_tag(filename='blog/extras/_recent_post.html',takes_context=True)
def recent_post(context,num=5):
    post_list = Post.objects.all().order_by('-create_time')[:num]
    return {
        'post_list': post_list
    }

@register.inclusion_tag(filename='blog/extras/_archives.html',takes_context=True)
def archives(context,):
    post_list = Post.objects.dates('create_time','month',order='DESC')
    return {
        'post_list': post_list
    }

@register.inclusion_tag(filename='blog/extras/_categories.html',takes_context=True)
def categories(context):
    categories = Category.objects.all()
    return {
        'categories': categories
    }

@register.inclusion_tag(filename='blog/extras/_tags.html',takes_context=True)
def tags(context,):
    tags = Tag.objects.all()
    return {
        'tags': tags
    }