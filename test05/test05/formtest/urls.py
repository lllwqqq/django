#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/23 上午11:18
@Author:  Aroma
@File: urls.py
@Software: PyCharm
"""
from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'formtest'

urlpatterns = [
    path('form',views.liuyan,name='liuyan'),
]