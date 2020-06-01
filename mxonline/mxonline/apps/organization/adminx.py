#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/1/9 下午2:14
@Author:  Aroma
@File: adminx.py
@Software: PyCharm
"""

import xadmin
from .models import CourseOrg, CityDict, Teacher


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'address', 'fav_nums', 'click_nums', 'image', 'add_time']
    search_fields = ['name', 'desc', 'address', 'fav_nums', 'click_nums', 'image']
    list_filter = ['name', 'desc', 'address', 'fav_nums', 'click_nums', 'image', 'add_time']


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class TeacherAdmin(object):
    list_display = ['name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums', 'org',
                    'add_time']
    search_fields = ['name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums', 'org']
    list_filter = ['name', 'work_years', 'work_company', 'work_position', 'points', 'fav_nums', 'click_nums', 'org',
                   'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
