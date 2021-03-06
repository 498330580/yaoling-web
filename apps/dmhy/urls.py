# -*- coding: utf-8 -*-
# @Time    : 2019-04-10-0010 23:35
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    re_path(r'search', search, name='search'),
    re_path(r'body', body, name='body')
]