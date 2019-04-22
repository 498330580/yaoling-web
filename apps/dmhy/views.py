from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import *

# Create your views here.


@login_required(login_url='/accounts/login')
# 分页代码
def get_page(request, post_list):
    paginator = Paginator(post_list, 80)
    try:
        page = int(request.GET.get('page', 1))
        post_list = paginator.page(page)
    except (InvalidPage, EmptyPage, PageNotAnInteger):
        post_list = paginator.page(1)
    return post_list


@login_required(login_url='/accounts/login')
def index(request):
    try:
        data = DmhyAll.objects.all().order_by('-time')
        dmhys = get_page(request, data)
        return render(request, 'dmhy/dmhy-list.html', locals())
    except Exception as e:
        print('动漫花园INDEX-ERROR', e)
