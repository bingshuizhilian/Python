#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：5.mysql '

__author__ = 'bingshuizhilian'



import pymysql

class MySql(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            db = 'douban',
            user = 'root',
            passwd = 'bs06271989',
            charset = 'utf8',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()

    def select(self, sql):
        try:
            self.cursor.execute(sql)
            print('Count:', self.cursor.rowcount)
            row = self.cursor.fetchone()
            while row:
                print('Row:', row)
                row = self.cursor.fetchone()
        except Exception as e:
            print('error occurred when execute select')
            print(e)


sqlSelectDemo = '''SELECT * FROM `movie_top250_3` WHERE star >= 9.5 OR star <= 4'''
query = MySql()
query.select(sqlSelectDemo)
