# -*- coding: utf-8 -*-
# @Time    : 2019-03-08- 0008 15:55
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.urls import path, include
from django.urls import path, include, re_path
from .views import *


urlpatterns = [
    re_path(r'^login/$', login, name='login'),
    re_path(r'^logout$', my_logout, name='logout'),
    re_path(r'register', register, name='register'),
    re_path(r'home', home, name='home'),
    re_path(r'index', index, name='index'),
    re_path(r'profile', profile, name='profile'),
    re_path(r'form_advanced', form_advanced, name='form_advanced'),
]

