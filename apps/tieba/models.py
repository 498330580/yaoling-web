from django.db import models
from django.utils import timezone

from accounts.models import MyUser

# from .tieba_time_task import *


# Create your models here.

# BDUSS设置
class Bduss(models.Model):
    user = models.ForeignKey(MyUser, verbose_name='用户', on_delete=models.CASCADE, editable=False)
    bduss = models.TextField(verbose_name='BDUSS')
    username = models.CharField(max_length=250, verbose_name='百度用户名', editable=False)
    usernames = models.CharField(max_length=250, verbose_name='百度用户名(验证用)', default='', editable=False)

    '''
    def save(self, *args, **kwargs):
        self.username = Tieba({'BDUSS': self.bduss}).get_name(self.bduss)
        super(Bduss, self).save(*args, **kwargs)
    '''

    class Meta:
        verbose_name = 'BDUSS设置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 个人贴吧列表
class TiebaMeList(models.Model):
    username = models.ForeignKey(Bduss, verbose_name='百度用户名', on_delete=models.CASCADE, editable=False)
    forum_name = models.CharField(max_length=250, verbose_name='名称', editable=False)
    forum_id = models.CharField(max_length=50, verbose_name='贴吧ID', editable=False)
    is_sign = models.BooleanField(verbose_name='是否签到', editable=False, help_text='判断该贴吧签到没有', default=False)
    user_exp = models.IntegerField(verbose_name='经验', editable=False)
    user_level = models.IntegerField(verbose_name='等级', editable=False)
    note = models.CharField(max_length=50, verbose_name='备注', editable=False, default='')

    class Meta:
        verbose_name = '贴吧列表'
        verbose_name_plural = verbose_name
        ordering = ['user_level']

    def __str__(self):
        return self.forum_name


# 贴吧签到时间
class SignTime(models.Model):
    name = models.ForeignKey(TiebaMeList, verbose_name='贴吧名字', on_delete=models.CASCADE, editable=False)
    time = models.DateTimeField(auto_now=True, verbose_name='签到时间', editable=False)

    class Meta:
        verbose_name = '签到时间'
        verbose_name_plural = verbose_name
        ordering = ['time']

    def __unicode__(self):
        return self.name


# 签到设置
class Signconfig(models.Model):
    user = models.OneToOneField(MyUser,  verbose_name='用户', on_delete=models.CASCADE, editable=False)
    baidu_zhidao = models.BooleanField(verbose_name='是否签到百度知道', editable=False, help_text='签到知道请打勾', default=False)
    baidu_wenku = models.BooleanField(verbose_name='是否签到百度文库', editable=False, help_text='签到文库请打勾', default=False)

    class Meta:
        verbose_name = '签到设置'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


# 失效BDUSS时间记录
class Bduss_time(models.Model):
    username = models.ForeignKey(Bduss, verbose_name='百度用户名', on_delete=models.CASCADE, editable=False)
    username_false = models.DateTimeField(verbose_name='BDUSS失效时间记录', editable=False, auto_now=True)
    email_send = models.DateTimeField(verbose_name='发送BDUSS失效邮件的时间记录', editable=False, auto_now_add=True)
    # email_state = models.BooleanField(verbose_name='是否已发送当日邮件', editable=False,  default=False)

    class Meta:
        verbose_name = '失效BDUSS时间记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username.username
