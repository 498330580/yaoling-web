# -*- coding: utf-8 -*-
# @Time    : 2019-05-12-0012 21:56
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : adminx.py
# @Software: PyCharm


import xadmin
from .models import *


class BdussAdmin:
    list_per_page = 10  # 每页显示10条，默认为100条
    list_display = ('username', 'bduss')    # 显示字段

    # 显示当前用户信息
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    # 保存当前用户为默认用户
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.user = request.user
            print(request.user)
            print(form.cleaned_data['bduss'])
        obj.save()


xadmin.site.register(Bduss, BdussAdmin)


class TiebaMeListAdmin:
    list_display = ('forum_name', 'forum_id', 'user_exp', 'user_level', 'is_sign', 'username', 'note')


xadmin.site.register(TiebaMeList, TiebaMeListAdmin)


class SignTimeAdmin:
    list_display = ('name', 'time')


xadmin.site.register(SignTime, SignTimeAdmin)
