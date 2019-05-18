from django.contrib.auth import logout

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.files.base import ContentFile
from django.http import HttpResponse

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
    SITE_DESC = settings.SITE_DESC
    SITE_KEY = settings.SITE_KEY
    STATISTICS = settings.STATISTICS
    if request.user.is_authenticated:
        myuser = MyUser.objects.get(username=request.user)
        superuser = True if request.user.is_superuser else False
        if not request.user.is_superuser:
            # 识别用户组名
            try:
                group = [i.name for i in Group.objects.filter(user=request.user)]
            except:
                group = '游客'
        else:
            group = '超级用户'
    return locals()


# 登录
def login(request):
    next = request.GET.get('next', '/accounts/home')
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
            return render(request, 'accounts/jump.html', locals())
    else:
        if request.user.is_authenticated:
            return render(request, 'accounts/body.html', locals())
        else:
            return render(request, 'accounts/login.html', locals())


# 注册
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
        user = MyUser()  # 创建用户对象
        user.username = username
        user.password = make_password(usr_paaaword)
        user.email = usr_email
        # user.is_staff = True    # 允许用户登录后台
        user.save()
        user = MyUser.objects.get(username=username)
        group = Group.objects.get(name='注册会员')
        user.groups.add(group)
        return render(request, 'accounts/jump.html', locals())
    else:
        next_url = request.GET.get('next', '/accounts/login')
        return render(request, 'accounts/register.html', locals())


# 注销
def my_logout(request):
    logout(request)
    url_jump = '/accounts/login'
    tips = '注销成功'
    return render(request, 'accounts/jump.html', locals())


# 个人主页
@login_required(login_url='/accounts/login')
def home(request):
    return render(request, 'accounts/body.html', locals())


# 个人主页首页
@login_required(login_url='/accounts/login')
def index(request):
    return render(request, 'accounts/index.html', locals())


# 修改个人资料
@login_required(login_url='/accounts/login')
def profile(request):
    if request.method == 'POST':
        try:
            img = request.FILES['avatar']
        except:
            img = False
        MyUser.objects.filter(username=request.user).update(
            qq=request.POST['qq'],
            mobile=request.POST['mobile'],
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
        )
        if img:
            myuser = MyUser.objects.get(username=request.user)
            file_content = ContentFile(img.read())
            myuser.avatar.save(img.name, file_content)
        tips = '资料修改成功'
    return render(request, 'accounts/profile.html', locals())


# 修改密码
@login_required(login_url='/accounts/login')
def form_password(request):
    if request.method == 'POST':
        # passworded = request.POST['passworded']
        password = request.POST['password']
        passwords = request.POST['passwords']
        tips = '密码修改成功'
        if 6 > len(password) or len(password) > 20:
            tips = '请输入正确的密码长度'
        if password != passwords:
            tips = '两次密码不同'
        if tips == '密码修改成功':
            user = MyUser.objects.get(username=request.user)
            user.password = make_password(password)
            user.save()
    return render(request, 'accounts/form_password.html', locals())


# 404页面
def page_not_found(request):
    return render(request, 'accounts/404.html')


# 500页面
def error(request):
    return render(request, 'accounts/500.html')
