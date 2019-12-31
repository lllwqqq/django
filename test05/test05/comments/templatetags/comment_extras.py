#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/20 下午5:58
@Author:  Aroma
@File: comment_extras.py
@Software: PyCharm
"""
from ..forms import CommentForm
from django import template

register = template.Library()


@register.inclusion_tag(filename='comment/inclusions/_comment_form.html', takes_context=True)
def comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'post': post,
        'form': form,
    }



