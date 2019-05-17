"""yaoling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
import xadmin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
# from sitemap import DmhyAllSitemap
from yaoling.settings import STATIC_ROOT, MEDIA_ROOT
# from django.contrib.sitemaps.views import sitemap


# sitemaps = {
#     'Dmhy': DmhyAllSitemap,
# }


urlpatterns = [
    path('', include(('gateway.urls', 'gateway'), namespace='gateway')),
    path('qiandao/', include(('tieba.urls', 'tieba'), namespace='qiandao')),
    path('dmhy/', include(('dmhy.urls', 'dmhy'), namespace='dmhy')),
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
    #         name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "accounts.views.page_not_found"
handler500 = "accounts.views.error"
