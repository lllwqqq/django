#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/20 下午1:45
@Author:  Aroma
@File: urls.py
@Software: PyCharm
"""
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.detail, name='detail'),
    path('posts/<int:year>/<int:month>/',views.archive,name='archive'),
    path('posts/category/<int:pk>/',views.categories,name='category'),
    path('posts/tag/<int:pk>/',views.tag,name='tag'),
]
