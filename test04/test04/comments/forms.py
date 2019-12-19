#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/18 下午3:48
@Author:  Aroma
@File: forms.py
@Software: PyCharm
"""

from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'url', 'text']
