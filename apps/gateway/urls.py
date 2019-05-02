# -*- coding: utf-8 -*-
# @Time    : 2019-03-08- 0008 17:37
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : urls.py
# @Software: PyCharm


from django.urls import path, include
from .views import index

urlpatterns = [
    path(r'', index, name='index'),
]
