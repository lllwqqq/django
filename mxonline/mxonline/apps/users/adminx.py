#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/1/6 下午2:01
@Author:  Aroma
@File: adminx.py
@Software: PyCharm
"""
from .models import EmailVerifyRecord, Banner
import xadmin
from xadmin.views import BaseAdminView,CommAdminView


class BaseSetting(object):
    '''
        后台管理系统支持切换主题
    '''
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    '''
    自定义后台管理系统左上角title及footer
    '''
    site_title = '知逸·礼 后台管理系统'
    site_footer = '知逸·知礼·知逸李'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(BaseAdminView, BaseSetting)
xadmin.site.register(CommAdminView, GlobalSettings)
