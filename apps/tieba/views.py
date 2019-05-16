# -*- coding: utf-8 -*-
# @Time    : 2019-03-13- 0013 11:17
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : urls.py
# @Software: PyCharm
from django.contrib.auth.models import Group
from django.shortcuts import render
# from django.utils import timezone
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import *
from .tieba_time_task import *


@login_required(login_url='/accounts/login')
# 用户组识别
def groups(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            group = True
        else:
            if Group.objects.get(user=request.user).name == '贴吧':
                group = True
            else:
                group = False
        return group


@login_required(login_url='/accounts/login')
# 分页代码
def get_page(request, post_list):
    paginator = Paginator(post_list, 20)
    try:
        page = int(request.GET.get('page', 1))
        post_list = paginator.page(page)
    except (InvalidPage, EmptyPage, PageNotAnInteger):
        post_list = paginator.page(1)
    return post_list


@login_required(login_url='/accounts/login')
# 贴吧签到首页
def tieba_index(request):
    try:
        if groups(request):
            bduss_int_False = Bduss.objects.filter(bduss='BDUSS无效', user=request.user)
            bduss_int_True = Bduss.objects.exclude(bduss='BDUSS无效').filter(user=request.user)
            tieba_is_sign_False = TiebaMeList.objects.filter(username__user__username=request.user,
                                                             is_sign=False).exclude(note='该贴吧无法签到，请检查贴吧设置。')
            tieba_is_sign_True = TiebaMeList.objects.filter(username__user__username=request.user, is_sign=True)
            tieba_is_sign_False_off = TiebaMeList.objects.filter(username__user__username=request.user,
                                                                 is_sign=False,
                                                                 note='该贴吧无法签到，请检查贴吧设置。'
                                                                 )
            return render(request, 'tieba/tieba-index.html', locals())
        else:
            return render(request, 'tieba/error.html')
    except Exception as e:
        print('贴吧签到首页ERROR', e)


# 判断用户是否登录
def login_on_off(request):
    try:
        if request.user.is_authenticated:
            return True
        else:
            return render(request, 'tieba/error.html', {'error': '请登录'})
    except Exception as e:
        print('登录判断：', e)
        return render(request, 'tieba/error.html', {'error': '请求错误'})


@login_required(login_url='/accounts/login')
def tieba_qiandao(request):
    # 一键签到
    if groups(request):
        try:
            for tieba_me_list in models.TiebaMeList.objects.filter(username__user__username=request.user):
                time_now = timezone.now()
                t_year = int(time_now.strftime("%Y"))
                t_month = int(time_now.strftime("%m"))
                t_day = int(time_now.strftime("%d"))
                time_list = models.SignTime.objects.filter(name=tieba_me_list,
                                                           time__day=t_day,
                                                           time__month=t_month,
                                                           time__year=t_year
                                                           )
                if tieba_me_list.is_sign:
                    # 判断本已签到贴吧是否添加签到时间，未添加就添加签到时间
                    tieba_me_list.note = ''
                    tieba_me_list.save()
                    if not time_list:
                        s = models.SignTime(name=tieba_me_list)
                        s.save()
                else:
                    tieba = Tieba(tieba_me_list.username.bduss).tieba_clock(name=tieba_me_list.forum_name,
                                                                            forum_id=tieba_me_list.forum_id)

                    if tieba:
                        # 顺利签到的情况
                        s = models.SignTime(name=tieba_me_list)
                        s.save()
                        tieba_me_list.is_sign = True
                        tieba_me_list.note = ''
                        tieba_me_list.save()
                    else:
                        # 无法签到的贴吧
                        if not time_list:
                            s = models.SignTime(name=tieba_me_list)
                            s.save()
                        tieba_me_list.note = '该贴吧无法签到，请检查贴吧设置。'
                        tieba_me_list.save()
            tips = '签到成功'
        except Exception as e:
            print('一键签到ERROR', e)
            tips = '签到失败 ERROR:%s' % e
        url_jump = '/tieba/tieba-like'
        return render(request, 'tieba/tieba-jump.html', locals())
    else:
        return render(request, 'tieba/error.html')


@login_required(login_url='/accounts/login')
def tieba_bduss_add(request):
    # 添加BDUSS
    if groups(request):
        bduss_list = Bduss.objects.filter(user=request.user).all()
        bduss_add = True
        if request.method == 'POST':
            bduss_add = False
            try:
                if request.POST:
                    bduss_new = request.POST.get('bduss', 1)
                    if bduss_new == 1 and request.POST.get('bduss_from'):
                        if Bduss.objects.filter(bduss=request.POST['bduss_from'], user=request.user):
                            bduss_on_off = '当前账户下，BDUSS已已存在，请勿重复添加'
                        else:
                            tieba_data = Tieba(request.POST['bduss_from'])
                            name = tieba_data.get_name()
                            if name != 'BDUSS无效':
                                bduss = Bduss()
                                bduss.user = request.user
                                bduss.bduss = request.POST['bduss_from']
                                bduss.username = name
                                bduss.save()
                                bduss_add = True
                            else:
                                bduss_on_off = 'BDUSS无效，请检查BDUSS有效性后添加'
                    return render(request, 'tieba/tieba-account.html', locals())
            except Exception as e:
                print('添加BDUSS ERROR', e)
                return render(request, 'tieba/tieba-account.html')
        else:
            return render(request, 'tieba/tieba-account.html', locals())
    else:
        return render(request, 'tieba/error.html')


@login_required(login_url='/accounts/login')
def tiebalist(request):
    # 贴吧列表
    if groups(request):
        try:
            # qiandao = False
            bduss_list = Bduss.objects.filter(user=request.user).exclude(username='BDUSS无效')
            tieba_me_list = []
            if request.method == 'POST':
                url_jump = request.get_full_path()
                if bduss_list:
                    for bduss in bduss_list:
                        for tieba in Tieba(bduss.bduss).tieba_me_list():
                            if TiebaMeList.objects.filter(username=bduss, forum_id=tieba['ID']):
                                # 更新贴吧数据
                                TiebaMeList.objects.filter(forum_id=tieba['ID'], username=bduss).update(
                                    is_sign=True if tieba['是否签到'] == '是' else False,
                                    user_exp=tieba['经验'],
                                    user_level=tieba['等级']
                                )
                            else:
                                # 添加贴吧数据
                                tieba_me_list.append(TiebaMeList(username=bduss,
                                                                 forum_name=tieba['名字'],
                                                                 forum_id=tieba['ID'],
                                                                 is_sign=True if tieba['是否签到'] == '是' else False,
                                                                 user_exp=tieba['经验'],
                                                                 user_level=tieba['等级']))
                    if tieba_me_list:
                        # 批量保存贴吧数据
                        TiebaMeList.objects.bulk_create(tieba_me_list)
                    tips = '更新贴吧数据成功'
                else:
                    # 没有符合条件的BDUSS
                    tips = '没有符合条件的BDUSS'
                return render(request, 'tieba/tieba-jump.html', locals())

            tieba_list_Q = TiebaMeList.objects.filter(username__user__username=request.user).exclude(username__username='BDUSS无效').order_by('user_level')
            tieba_list = tieba_list_Q.values()
            tieba_time_list = []
            for tieba_me, tieba_me_Q in zip(tieba_list, tieba_list_Q):
                tieba_me['username'] = tieba_me_Q.username
                signtime = SignTime.objects.filter(name=tieba_me['id']).order_by('-time').values()[:1]
                if signtime:
                    tieba_me['time'] = signtime[0]['time']
                    tieba_time_list.append(tieba_me)
                else:
                    tieba_me['time'] = '未签到'
                    tieba_time_list.append(tieba_me)
            contacts = get_page(request, tieba_time_list)
            return render(request, 'tieba/tieba-like-list.html', locals())
        except Exception as e:
            print('贴吧列表ERROR', e)
            tips = '贴吧列表ERROR:%s' % e
            url_jump = request.get_full_path()
            return render(request, 'tieba/tieba-jump.html')
    else:
        return render(request, 'tieba/error.html')


# 签到设置
@login_required(login_url='/accounts/login')
def signconfig(request):
    try:
        if groups(request):
            if request.method == 'POST':
                zhidao = request.POST['zhidao']
                wenku = request.POST['wenku']
                if Signconfig.objects.filter(user=request.user):
                    if zhidao == 'yes' and wenku == 'yes':
                        Signconfig.objects.filter(user=request.user).update(baidu_zhidao=True, baidu_wenku=True)
                    elif zhidao == 'yes' and wenku == 'no':
                        Signconfig.objects.filter(user=request.user).update(baidu_zhidao=True, baidu_wenku=False)
                    elif zhidao == 'no' and wenku == 'yes':
                        Signconfig.objects.filter(user=request.user).update(baidu_zhidao=False, baidu_wenku=True)
                    else:
                        Signconfig.objects.filter(user=request.user).update(baidu_zhidao=False, baidu_wenku=False)
                    tips = '更新成功'
                else:
                    signconfig = Signconfig()
                    signconfig.user = request.user
                    signconfig.baidu_wenku = True if wenku == 'yes' else False
                    signconfig.baidu_zhidao = True if zhidao == 'yes' else False
                    signconfig.save()
                    tips = '保存成功'
                url_jump = request.get_full_path()
                return render(request, 'tieba/tieba-jump.html', locals())
            else:
                if Bduss.objects.filter(user=request.user):
                    bduss = False
                    if Signconfig.objects.filter(user=request.user):
                        signconfigs = Signconfig.objects.get(user=request.user)
                        baidu_zhidao = signconfigs.baidu_zhidao
                        baidu_wenku = signconfigs.baidu_wenku
                    else:
                        render(request, 'tieba/tieba-config.html')
                else:
                    bduss = True
                return render(request, 'tieba/tieba-config.html', locals())
        else:
            return render(request, 'tieba/error.html')
    except Exception as e:
        print('签到设置ERROR', e)
