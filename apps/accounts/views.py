from django.contrib.auth import logout

# Create your views here.

from django.shortcuts import render
from django.conf import settings
from re import search
from accounts.models import MyUser
# from hashlib import sha256
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth


# 网站公共参数
def global_setting(request):
    SITE_NAME = settings.SITE_NAME
    return locals()


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            url_jump = request.POST['next']
            auth.login(request, user)
            request.session['user'] = username
            tips = '登录成功'
            return render(request, 'accounts/jump.html', locals())
        else:
            tips = '登录失败'
            url_jump = request.get_full_path()
            return render(request, 'accounts/jump.html', locals())
    else:
        next = request.GET.get('next', '/')
        return render(request, 'accounts/login.html', locals())


def register(request):
    if request.method == 'POST':
        username = request.POST['usr_name']
        usr_paaaword = request.POST['usr_password']
        usr_password_check = request.POST['usr_password_check']
        usr_email = request.POST['usr_email']
        xieyi = request.POST.getlist('xieyi')
        re_email = r"[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
        url_jump = request.get_full_path()
        # 判断是否输入用户名
        if not username:
            tips = '用户名不能为空'
            return render(request, 'accounts/jump.html', locals())
        # 判断用户名个是否已存在
        if MyUser.objects.filter(username=username):
            tips = '用户名已存在'
            return render(request, 'accounts/jump.html', locals())
        # 判断密码是否为正确长度
        if 6 > len(usr_paaaword) or len(usr_paaaword) > 20:
            tips = '请输入正确的密码长度'
            return render(request, 'accounts/jump.html', locals())
        # 判断两次密码是否相同
        if usr_paaaword != usr_password_check:
            tips = '两次密码不同'
            return render(request, 'accounts/jump.html', locals())
        # 判断是否同意协议
        if not xieyi:
            tips = '未同意协议'
            return render(request, 'accounts/jump.html', locals())
        # 判断是否输入了正确的邮箱
        if not search(re_email, usr_email):
            tips = '未请输入正确的邮箱'
            return render(request, 'accounts/jump.html', locals())
        # 判断邮箱是否存在
        if MyUser.objects.filter(email=usr_email):
            tips = '邮箱已存在'
            return render(request, 'accounts/jump.html', locals())
        # 注册成功
        tips = '注册成功'
        url_jump = request.POST['next_url']
        # s1 = sha256()
        # s1.update(usr_paaaword.encode('utf-8'))
        # password = s1.hexdigest()
        user = MyUser()     # 创建用户对象
        user.username = username
        user.password = make_password(usr_paaaword)
        user.email = usr_email
        user.is_staff = True
        user.save()
        return render(request, 'accounts/jump.html', locals())
    else:
        next_url = request.GET.get('next', '/accounts/login')
        return render(request, 'accounts/register.html', locals())


def my_logout(request):
    logout(request)
    url_jump = '/accounts/login'
    tips = '注销成功'
    return render(request, 'accounts/jump.html', locals())
