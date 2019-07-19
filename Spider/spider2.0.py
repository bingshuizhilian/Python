#coding:utf-8

import requests
import urllib.request
import os
import re
import datetime as dt

def getHtmlStr(url):
    headers = {
    'user-agent': 'Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.4882.400QQBrowser / 9.7.13059.400'
    }
    response = requests.get(url, headers = headers)
    # print(response.status_code)
    # print(response.text)
    return response.text

def writeToFile(str, filename, path):
    if not os.path.exists(path):
        os.makedirs(path)
    pageFile = open(path + filename + '.txt', 'w', encoding = 'utf-8')
    pageFile.write(str)
    pageFile.close()

# writeToFile(getHtmlStr(testUrl), 'tieba', saveFilePath)

def downloadPictures(url, save_path):
    # regex = r'src="(http.+?\.jpg)"'
    regex = r'src="(http[^ ]+?\.jpg)" '
    regexImg = re.compile(regex)
    imgList = regexImg.findall(getHtmlStr(url))

    n = 0
    for img in imgList:
        print('_%d_' % n, img)
        n += 1

    if not os.path.exists(save_path):
            os.makedirs(save_path)

    x = 0
    for img in imgList:
        urllib.request.urlretrieve(img, save_path + '%s.jpg' %x)
        x += 1

testUrl = r'http://tieba.baidu.com/p/1753935195'
testTiebaUrl = r'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A3%81%E7%BA%B8'
curFilePath = os.path.dirname(__file__)
saveFilePathTest = curFilePath + '/savedFiles/'
curExePath = os.getcwd()
saveFilePath = curExePath + '/savedFiles/' + dt.datetime.now().strftime(r'%Y%m%d-%H%M%S/')

# downloadPictures(testUrl, saveFilePath)

def userGetPicture(save_path):
    print('-' * 10 ,r'网页图片抓取', '-' * 10)
    url = input(r'请输入某个帖子的url:')
    if url:
        print('-' * 10 ,r'开始抓取', '-' * 10)
        downloadPictures(url, save_path)
        print('-' * 10 ,r'下载成功', '-' * 10)
        os.system("explorer.exe %s" % os.path.realpath(save_path))
    else:
        pass
    
    input(r'按任意键结束')

def userGetPicturesByPostID(save_path, max_download = 10):
    print('-' * 10 ,r'百度贴吧图片抓取', '-' * 10)
    url = input(r'请输入某个贴吧的url:')
    regex = r'data-field=\'{&quot;id&quot;:(\d+?),' # data-field="{"id":(\d+?),|data-field=\'{&quot;id&quot;:(\d+?),
    regexPostID = re.compile(regex)
    postIdList = regexPostID.findall(getHtmlStr(url))
    urlList = []

    # print(postIdList)
    for i in range(len(postIdList)):
        urlList.append(r'http://tieba.baidu.com/p/' + postIdList[i])
    # print(urlList)

    if not os.path.exists(os.path.realpath(save_path)):
        os.makedirs(os.path.realpath(save_path))

    n = 0
    for i in range(max_download):
        if n < len(postIdList):
            n += 1
        else:
            break

        if not os.path.exists(os.path.realpath(save_path + postIdList[i])):
            os.makedirs(os.path.realpath(save_path + postIdList[i]))

        print('\n' + '-' * 10 ,r'开始抓取' + postIdList[i], '-' * 10)
        downloadPictures(urlList[i], save_path + postIdList[i] + '/')
        print('-' * 10 ,r'下载成功' + postIdList[i], '-' * 10)

    os.system("explorer.exe %s" % os.path.realpath(save_path))
    input(r'按任意键结束')

if __name__ == "__main__":
    choice = input('请输入要抓取的类型 1->单个帖子，2->某个贴吧：')
    choice = int(choice)

    if 1 == choice:
        userGetPicture(saveFilePath)
    elif 2 == choice:
        cnt = input('请输入本次最多希望抓取的帖子数：')
        if int(cnt) > 0:
            userGetPicturesByPostID(saveFilePath, int(cnt))
    else:
        pass
