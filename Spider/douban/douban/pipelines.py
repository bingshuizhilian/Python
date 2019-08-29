# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql.cursors
from scrapy import cmdline

class DoubanPipeline(object):
    def __init__(self):
        # 连接数据库
        # 开启管道写入mysql需要在settings.py中打开ITEM_PIPELINES的注释
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

    def process_item(self, item, spider):
        self.cursor.execute(
            '''insert into movie_top250_3(title, movieInfo, star, evaluation, quote)
            value (%s, %s, %s, %s, %s)''',
            (
                item['title'],
                item['movieInfo'],
                item['star'],
                item['evaluation'],
                item['quote']
            )
        )
        self.connect.commit()

        return item
