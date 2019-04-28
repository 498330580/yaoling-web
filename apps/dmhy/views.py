from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .models import *

# Create your views here.


@login_required(login_url='/accounts/login')
# 分页代码（自带分页器）
def get_page(request, post_list):
    paginator = Paginator(post_list, 80)
    try:
        page = int(request.GET.get('page', 1))
        post_list = paginator.page(page)
    except (InvalidPage, EmptyPage, PageNotAnInteger):
        post_list = paginator.page(1)
    return post_list


# 自带分页器主页
@login_required(login_url='/accounts/login')
def index1(request):
    try:
        data = DmhyAll.objects.all().order_by('-time')
        dmhys = get_page(request, data)
        return render(request, 'dmhy/dmhy-list.html', locals())
    except Exception as e:
        print('动漫花园INDEX-ERROR', e)


# 高效分页器
@login_required(login_url='/accounts/login')
def index(request):
    ONE_PAGE_OF_DATA = 80
    try:
        page = int(request.GET.get('page', 1))
        pageType = str(request.GET.get('pageType', ''))
        allPage = int(request.GET.get('allPage', '1'))
    except ValueError:
        page = 1
        allPage = 1
        pageType = ''

    if pageType == 'pageDown':
        page += 1
    elif pageType == 'pageUp':
        page -= 1

    startPos = (page - 1) * ONE_PAGE_OF_DATA
    endPos = startPos + ONE_PAGE_OF_DATA
    dmhys = DmhyAll.objects.all()[startPos:endPos]

    if page == 1 and allPage == 1:  # 标记1
        allPostCounts = DmhyAll.objects.count()
        allPage = allPostCounts // ONE_PAGE_OF_DATA
        remainPost = allPostCounts % ONE_PAGE_OF_DATA
        if remainPost > 0:
            allPage += 1

    return render(request, "dmhy/dmhy-list.html", locals())
