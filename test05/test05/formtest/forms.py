#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2019/12/23 上午11:18
@Author:  Aroma
@File: forms.py
@Software: PyCharm
"""

from .models import UserInfo
from django import forms

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'age', 'sex', 'addr', 'school']
