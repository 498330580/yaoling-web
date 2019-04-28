from django.contrib.auth import logout
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.conf import settings


# 网站公共参数
def global_setting(request):
    SITE_NAME = settings.SITE_NAME
    return locals()


def login(request):
    next = request.GET.get('next')
    return render(request, 'accounts/login.html', locals())


def register(request):
    return render(request, 'accounts/register.html', locals())


def my_logout(request):
    logout(request)
    url_jump = '/accounts/login'
    tips = '注销成功'
    return render(request, 'accounts/jump.html', locals())
