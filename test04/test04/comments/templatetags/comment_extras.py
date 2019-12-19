#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/18 下午3:51
@Author:  Aroma
@File: comment_extras.py
@Software: PyCharm
"""
from django import template
from ..forms import CommentForm

register = template.Library()


@register.inclusion_tag(filename='comments/inclusions/_forms.html', takes_context=True)
def comment_form(context, post, form=None):
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }
