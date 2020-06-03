#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/3 下午10:06
@Author:  Aroma
@File: urls.py
@Software: PyCharm
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
]