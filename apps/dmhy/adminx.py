# -*- coding: utf-8 -*-
# @Time    : 2019-05-11-0011 18:19
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : adminx.py
# @Software: PyCharm


import xadmin
from .models import DmhyAll


class DmhyAllAdmin:
    list_display = ['name', 'time', 'zimuzu', 'fenlei', 'faburen', 'xiazai_url',]


xadmin.site.register(DmhyAll, DmhyAllAdmin)
