#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/1 上午10:15
@Author:  Aroma
@File: urls.py
@Software: PyCharm
"""

from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/',views.detail,name='detail') ,
    path('archives/<int:year>/<int:month>/',views.archives,name='archives'),
    path('categories/<int:pk>/',views.categories,name='categories'),
    path('tags/<int:pk>/',views.tag,name='tag'),

]

