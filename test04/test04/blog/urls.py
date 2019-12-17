#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/10 下午5:25
@Author:  Aroma
@File: urls.py
@Software: PyCharm
"""


from . import views
from django.urls import path


app_name = 'blog'
urlpatterns = [
    path('',views.index,name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('posts/<int:year>/<int:month>/', views.archive, name='archive'),
    path('category/<int:pk>/', views.category, name='category'),
    path('tag/<int:pk>/', views.tag, name='tag'),
]