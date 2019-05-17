# -*- coding: utf-8 -*-
# @Time    : 2019-05-17-0017 20:24
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : sitemap.py
# @Software: PyCharm


from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps import GenericSitemap
from django.urls import reverse
from dmhy.models import DmhyAll


# class StaticViewSitemap(Sitemap):
#     priority = 0.5
#     changefreq = 'daily'
#
#     def items(self):
#         return ['blog:index', ]
#
#     def location(self, item):
#         return reverse(item)


class DmhyAllSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return DmhyAll.objects.all()

    def lastmod(self, obj):
        return obj.pub_date
