# -*- coding: utf-8 -*-
# @Time    : 2019/10/21 上午12:37
# @Author  : Thanlon
# @Wechat：18512152005
# @Email   : thanlon@sina.com
# @File    : settings.py
# @Software: PyCharm
from DBUtils.PooledDB import PooledDB
import pymysql


class Config(object):
    pass


class ProductionConfig(Config):
    DEBUG = False
    POOL = PooledDB(
        creator=pymysql,
        maxconnections=6,
        mincached=2,
        maxcached=5,
        maxshared=3,
        blocking=True,
        maxusage=None,
        setsession=[],
        ping=0,
        host='106.12.115.136',
        port=3307,
        user='thanlon',
        password='39kiku',
        database='39bysj',
        charset='utf8'
    )


class DevelopmentConfig(Config):
    DEBUG = True
    POOL = PooledDB(
        creator=pymysql,
        maxconnections=6,
        mincached=2,
        maxcached=5,
        maxshared=3,
        blocking=True,
        maxusage=None,
        setsession=[],
        ping=0,
        host='106.12.115.136',
        port=3307,
        user='thanlon',
        password='39kiku',
        database='39bysj',
        charset='utf8'
    )


class TestingConfig(Config):
    DEBUG = True
