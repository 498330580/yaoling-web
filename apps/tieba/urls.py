# -*- coding: utf-8 -*-
# @Time    : 2019-03-13- 0013 11:17
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : urls.py
# @Software: PyCharm


from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    path('', tieba_index, name='date'),
    path('index', tieba_index, name='index'),
    path('tieba-account', tieba_bduss_add, name='tieba-account'),
    re_path(r'^tieba-like$', tiebalist, name='tieba-like'),
    path('tieba-sign', tieba_qiandao, name='tieba-sign'),
    path('tieba-signconfig', signconfig, name='signconfig'),
    path('tieba-bduss', tieba_bduss, name='tieba-bduss')
]

