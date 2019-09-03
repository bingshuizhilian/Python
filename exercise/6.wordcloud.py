#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：6.wordcloud '

__author__ = 'bingshuizhilian'



# 参考：https://www.cnblogs.com/ZaraNet/p/10136589.html

import pymysql

from wordcloud import WordCloud
import PIL.Image as image
import numpy as np
import jieba as jb

def trans_CN(text):
    word_list = jb.cut(text)
    result = ' '.join(word_list)
    return result

with open('E:/GITHUB/Python/exercise/6.wordcloud-words-ch.txt', encoding='utf-8') as f:
    text = f.read()
    text = trans_CN(text)
    # print(text)
    mk = np.array(image.open('E:/GITHUB/Python/exercise/6.wordcloud-china.jpg'))
    #将文本放入WordCoud容器对象中并分析
    wc = WordCloud(mask=mk, font_path = 'C:/Windows/Fonts/msyh.ttc').generate(text)
    img_produce = wc.to_image()
    img_produce.show()
    img_produce.save('E:/GITHUB/Python/exercise/6.wordcloud-result.bmp', format='bmp')
    