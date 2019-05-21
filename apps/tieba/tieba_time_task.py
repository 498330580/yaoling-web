# -*- coding: utf-8 -*-
# @Time    : 2019-03-22- 0022 17:34
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : tieba_time_task.py
# @Software: PyCharm


import os, sys
import random
import re
import time

import django
import requests as req

# 当前脚本目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 设置当前工作目录为脚本目录
# os.chdir('/www/wwwroot/python/yaoling')
# print('当前脚本目录',BASE_DIR,'当前工作目录',os.getcwd())
# 将django项目根目录加入环境变量
parent_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(parent_path)

# 在默认的环境中运行（第一个参数是Django运行的配置文件，第二个参数是当前项目运行的配置文件）
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yaoling.settings")
# 运行Django项目
django.setup()

from tieba import models
from django.utils import timezone


class Tieba:
    def __init__(self, bduss):
        self.wenku = req.Session()
        self.zhidao = req.Session()
        self.tieba_qiandao = req.Session()
        self.tieba = req.Session()
        self.wenku.headers.update({
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'BDUSS=' + bduss,
            'Host': 'wenku.baidu.com',
            'Referer': 'https://wenku.baidu.com/task/browse/daily',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.181 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        })
        self.zhidao.headers.update({
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '11',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'BDUSS=' + bduss,
            'Host': 'zhidao.baidu.com',
            'Origin': 'https://zhidao.baidu.com',
            'Referer': 'https://zhidao.baidu.com/mmisc/signinfo?uid=C1954D0D376337B302790226BF0B702F&step=2',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, '
                          'like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'X-ik-ssl': '1',
            'X-Requested-With': 'XMLHttpRequest',
        })
        self.tieba_qiandao.headers.update({
                'Host': 'tieba.baidu.com',
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, '
                              'like Gecko) Chrome/72.0.3626.109 Mobile Safari/537.36 ',
                'Cookie': 'BDUSS=' + bduss,
            })
        self.tieba.cookies.update({'BDUSS': bduss})
        self.tieba.headers.update({
            'Host': 'tieba.baidu.com',
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/39.0.2171.71 Safari/537.36',
        })

    def baidu_wenku(self, time_sleep=True):
        # 百度文库签到
        if time_sleep:
            time.sleep(random.randint(1, 5))  # 随机间隔签到时间
        url = 'https://wenku.baidu.com/task/submit/signin'
        self.wenku.get(url)
        return '签到成功'

    def baidu_zhidao(self, time_sleep=True):
        # 百度知道签到
        if time_sleep:
            time.sleep(random.randint(1, 5))  # 随机间隔签到时间
        url = 'https://zhidao.baidu.com/msubmit/signin?random=0.3507959078709957&'
        payload = {"ssid": "", "cifr": ""}
        if self.zhidao.post(url, data=payload).json()['errmsg'] != '已签到':
            errmsg = '签到成功'
        else:
            errmsg = '已签到'
        return errmsg

    def tieba_login_error(self):
        # 检查bduss是否失效
        if self.tieba.get('http://tieba.baidu.com/dc/common/tbs').json()['is_login']:
            return True
        else:
            return False

    def bduss_id(self):
        # 获取贴吧用户中心网页拼接ID,并合成用户中心地址
        try:
            r = self.tieba_qiandao.get('http://tieba.baidu.com/f/user/json_userinfo').json()['data']['user_portrait']
            tieba_yonghu_url = 'http://tieba.baidu.com/home/main?id=' + r
            return tieba_yonghu_url
        except Exception as e:
            print('获取贴吧用户中心网页拼接ID error', e)
            return 'https://tieba.baidu.com/index.html'

    def get_name(self):
        # 网页版获取贴吧用户名
        try:
            r = self.tieba.get('https://tieba.baidu.com/mo/q-').text
            name_re = re.search(r">([\u4e00-\u9fa5a-zA-Z0-9]+)的i贴吧<", r)
            if name_re:
                name = re.search(r">([\u4e00-\u9fa5a-zA-Z0-9]+)的i贴吧<", r).group(1)
            else:
                name = 'BDUSS无效'
        except Exception as e:
            print('网页版获取贴吧用户名error:', e)
            name = 'BDUSS无效'
        return name

    # 获取账号的关注贴吧列表
    def tieba_me_list(self):
        try:
            tieba_list = []
            html_list = self.tieba.get('http://tieba.baidu.com/mo/q/newmoindex').json()
            for i in html_list['data']['like_forum']:
                tieba_list.append({'ID': i['forum_id'],
                                   '名字': i['forum_name'],
                                   '是否签到': '是' if i['is_sign'] == 1 else '否',
                                   '经验': i['user_exp'],
                                   '等级': i['user_level'],
                                   '是否关注': '是' if i['is_like'] else '否'})
            return tieba_list
        except Exception as e:
            print('获取账号的关注贴吧列表error:', e)

    # 签到贴吧，并返回是否签到成功
    def tieba_clock(self, name, forum_id, time_sleep=True):
        try:
            if time_sleep:
                time.sleep(random.randint(1, 5))      # 随机间隔签到时间
            t = re.search('"tbs":"(.*?)"', self.tieba_qiandao.get('https://tieba.baidu.com/f?kw=%s&pn=0&' % name).text)
            if t:
                tbs = t.group(1)
                is_like = 1
                qiandao = self.tieba.get('https://tieba.baidu.com/mo/q/sign?tbs=%s&kw=%s&is_like=%d&fid=%d' % (tbs,
                                                                                                               name,
                                                                                                               is_like,
                                                                                                               int(forum_id)))
                time.sleep(2)
                if qiandao.json()['data']['msg'] != '亲，你之前已经签过了':
                    # 顺利签到的情况
                    return True
            else:
                # 无法签到的贴吧
                return False
        except Exception as e:
            print('签到贴吧error', e)
            return False


class Task:
    @staticmethod
    def bduss_error():
        # 定时检测数据库中BDUSS是否有效
        print('开始检查BDUSS有效性')
        bduss_list = models.Bduss.objects.all()
        for bduss in bduss_list:
            name = Tieba(bduss.bduss).get_name()
            bduss = models.Bduss.objects.filter(bduss=bduss.bduss)
            bduss.update(username=name)
        print('BDUSS有效性检查结束')

    @staticmethod
    def bduss_delete():
        # 定时删除数据库中失效的BDUSS
        print('开始删除失效的BDUSS')
        models.Bduss.objects.filter(username='BDUSS无效').delete()
        print('删除失效的BDUSS完毕')

    @staticmethod
    def tieba_me_list_update():
        # 定时更新个人贴吧列表数据
        try:
            print('开始更新贴吧信息')
            bduss_list = models.Bduss.objects.exclude(username='BDUSS无效')
            tieba_me_list = []
            if bduss_list:
                for bduss in bduss_list:
                    for tieba_me in Tieba(bduss.bduss).tieba_me_list():
                        if models.TiebaMeList.objects.filter(username=bduss, forum_id=tieba_me['ID']):
                            models.TiebaMeList.objects.filter(username=bduss, forum_id=tieba_me['ID']).update(
                                is_sign=True if tieba_me['是否签到'] == '是' else False,
                                user_exp=tieba_me['经验'],
                                user_level=tieba_me['等级']
                            )
                        else:
                            tieba_me_list.append(models.TiebaMeList(username=bduss,
                                                                    forum_name=tieba_me['名字'],
                                                                    forum_id=tieba_me['ID'],
                                                                    is_sign=True if tieba_me['是否签到'] == '是' else False,
                                                                    user_exp=tieba_me['经验'],
                                                                    user_level=tieba_me['等级']))
                if tieba_me_list:
                    models.TiebaMeList.objects.bulk_create(tieba_me_list)
            print('更新贴吧信息结束')
        except Exception as e:
            print('定时更新个人贴吧列表数据ERROR:', e)

    @staticmethod
    def tieba_timing_task():
        # 定时签到
        try:
            print('开始定时签到贴吧')
            for tieba_me_list in models.TiebaMeList.objects.all():
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
            print('定时签到贴吧结束')
        except Exception as e:
            print('定时签到error：', e)

    @staticmethod
    def baidu_wenku_sign():
        # 定时签到文库
        try:
            print('开始定时签到文库')
            bduss_list = models.Bduss.objects.exclude(username='BDUSS无效').filter(user__signconfig__baidu_wenku=True)
            for bduss in bduss_list:
                Tieba(bduss.bduss).baidu_wenku()
            print('定时签到文库结束')
        except Exception as e:
            print('定时签到文库ERROR', e)

    @staticmethod
    def baidu_zhidao_sign():
        # 定时签到知道
        try:
            print('开始定时签到知道')
            bduss_list = models.Bduss.objects.exclude(username='BDUSS无效').filter(user__signconfig__baidu_zhidao=True)
            for bduss in bduss_list:
                Tieba(bduss.bduss).baidu_zhidao()
            print('定时签到知道结束')
        except Exception as e:
            print('定时签到知道ERROR', e)


def run():
    Task.bduss_error()
    Task.bduss_delete()
    Task.tieba_me_list_update()
    Task.tieba_timing_task()
    Task.baidu_wenku_sign()
    Task.baidu_zhidao_sign()


if __name__ == '__main__':
    # Task.bduss_error()
    # Task.bduss_delete()
    # Task.tieba_me_list_update()
    # Task.tieba_timing_task()
    # Task.baidu_wenku_sign()
    # Task.baidu_zhidao_sign()
    run()
