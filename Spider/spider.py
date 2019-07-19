#coding:utf-8

import urllib.request
import os
import re

def getHtmlStr(url):
    page = urllib.request.urlopen(url)
    htmlcode = page.read()
    htmlcode = str(htmlcode, encoding = 'utf-8')
    return htmlcode

def writeToFile(str, filename, path):
    if not os.path.exists(path):
        os.makedirs(path)
    pageFile = open(path + filename + '.txt', 'w')
    pageFile.write(str)
    pageFile.close()

# writeToFile(getHtmlStr(testUrl), 'tieba', saveFilePath)

def downloadPictures(url, save_path):
    # regex = r'src="(.+?\.jpg)"'
    regex = r'src="([^ ]+?\.jpg)" '
    regexImg = re.compile(regex)
    imgList = regexImg.findall(getHtmlStr(url))

    if not os.path.exists(save_path):
            os.makedirs(save_path)

    x = 0
    for img in imgList:
        print(img)
        urllib.request.urlretrieve(img, save_path + '%s.jpg' %x)
        x += 1

testUrl = 'http://tieba.baidu.com/p/1753935195'
# curFilePath = os.path.dirname(__file__)
curExePath = os.getcwd()
saveFilePath = curExePath + '/savedFiles/'

# downloadPictures(testUrl, saveFilePath)

def userGetPicture(save_path):
    print('-' * 10 ,r'网页图片抓取', '-' * 10)
    url = input(r'请输入url:')
    if url:
        print('-' * 10 ,r'开始抓取', '-' * 10)
        downloadPictures(url, save_path)
        print('-' * 10 ,r'下载成功', '-' * 10)
        os.system("explorer.exe %s" % os.path.realpath(save_path))
    else:
        pass
    
    input(r'按任意键结束')

userGetPicture(saveFilePath)
