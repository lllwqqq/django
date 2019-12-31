#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/20 下午5:56
@Author:  Aroma
@File: forms.py
@Software: PyCharm
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']


