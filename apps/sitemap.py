# -*- coding: utf-8 -*-
# @Time    : 2019-05-17-0017 20:24
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : sitemap.py
# @Software: PyCharm


from django.contrib.sitemaps import Sitemap
from dmhy.models import DmhyAll
from gateway.models import Guide


class DmhyAllSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return DmhyAll.objects.all()

    def lastmod(self, obj):
        return obj.time


class GuideSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Guide.objects.filter(category__name='本站导航')

    def lastmod(self, obj):
        return obj.date_publish
