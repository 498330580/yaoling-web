# -*- coding: utf-8 -*-
# @Time    : 2019-04-09-0009 21:42
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : mongo_mysql.py
# @Software: PyCharm
import datetime
import os

import pymysql
import pymongo
import django
# 在默认的环境中运行（第一个参数是Django运行的配置文件，第二个参数是当前项目运行的配置文件）
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yaoling.settings")
# 运行Django项目
django.setup()

from dmhy import models
from django.utils import timezone


def mongo():
    try:
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['yaoling-scrapy']
        collection = db['dmhyopen']
        datas = collection.find({}, no_cursor_timeout=True)
        data_list = []
        for data in datas:
            data_list.append(data)
        client.close()
        return data_list
    except Exception as e:
        print('error', e)


def mysql(data):
    try:
        if not models.DmhyAll.objects.filter(name_url=data['name_url']):
            dmhy = models.DmhyAll()
            dmhy.name_url = data['name_url']
            dmhy.name = data['name']
            dmhy.zimuzu = data['zimuzu']
            dmhy.zimuzu_url = data['zimuzu_url']
            dmhy.xiazai_url = data['xiazai_url']
            dmhy.faburen = data['faburen']
            dmhy.fenlei = data['fenlei']
            dmhy.time = datetime.datetime.strptime(data['time'], '%Y/%m/%d %H:%M')
            dmhy.daxiao = data['daxiao']
            dmhy.faburen_url = data['faburen_url']
            dmhy.save()
        else:
            print(data['name'], '已存在')
    except Exception as e:
        print('ERROR', e)


if __name__ == '__main__':
    datas = mongo()
    for data in datas:
        mysql(data)
    print('转移完成')
