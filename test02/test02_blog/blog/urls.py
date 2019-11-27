#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/11/27 下午5:38
@Author:  Aroma
@File: urls.py
@Software: PyCharm
"""

from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
]
