# -*- coding: utf-8 -*-
# @Time    : 2019-05-12-0012 21:53
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : adminx.py
# @Software: PyCharm

import xadmin
from .models import *


class GuideAdmin:
    list_display = ('title', 'callback_url', 'description', 'category', 'date_publish', 'index')


xadmin.site.register(Guide, GuideAdmin)


class CategoryAdmin:
    list_display = ('name',)


xadmin.site.register(Category, CategoryAdmin)
