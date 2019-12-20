#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/20 下午1:45
@Author:  Aroma
@File: urls.py
@Software: PyCharm
"""
from django.urls import path
from . import  views
urlpatterns = [
    path('',views.index,name='index'),
]