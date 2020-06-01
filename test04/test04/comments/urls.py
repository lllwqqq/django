#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/19 下午4:38
@Author:  Aroma
@File: urls.py
@Software: PyCharm
"""
from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]