#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/1/9 下午1:39
@Author:  Aroma
@File: adminx.py
@Software: PyCharm
"""
import xadmin

from .models import Courses, Video, CourseResource, Lesson


class CoursesAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'image',
                    'add_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'image']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'click_nums', 'image',
                   'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['name', 'course']
    list_filter = ['course__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['name', 'course', 'download', 'add_time']
    search_fields = ['name', 'course', 'download']
    list_filter = ['name', 'course', 'download', 'add_time']


class VideoAdmin(object):
    list_display = ['name', 'lesson', 'add_time']
    search_fields = ['name', 'lesson']
    list_filter = ['name', 'lesson', 'add_time']


xadmin.site.register(Courses, CoursesAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
