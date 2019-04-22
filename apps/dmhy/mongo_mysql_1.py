# -*- coding: utf-8 -*-
# @Time    : 2019-04-09-0009 21:42
# @Author  : Andy
# @Email   : 498330580@qq.com
# @File    : mongo_mysql.py
# @Software: PyCharm
import datetime

import pymysql
import pymongo



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
	db = pymysql.connect(user='root', password='19920124Zhy@.', db='yaoling')
	cursor =db.cursor()
	sql = "SELECT * FROM dmhy_dmhyall WHERE name_url = '{url}';".format(url=data['name_url'])
	cursor.execute(sql)
    try:
        if not cursor.rowcount:
            name_url = data['name_url']
            name = data['name']
            zimuzu = data['zimuzu']
            zimuzu_url = data['zimuzu_url']
            xiazai_url = data['xiazai_url']
            faburen = data['faburen']
            fenlei = data['fenlei']
            time = datetime.datetime.strptime(data['time'], '%Y/%m/%d %H:%M')
            daxiao = data['daxiao']
            faburen_url = data['faburen_url']
            sql = 'INSER INTO yaoling(name_url,name,zimuzu,zimuzu_url,xiazai_url,faburen,fenlei,time,daxiao,faburen_url) values()'
        else:
            print(data['name'], '已存在')
    except Exception as e:
        print('ERROR', e)


if __name__ == '__main__':
    datas = mongo()
    for data in datas:
        mysql(data)
    print('转移完成')
