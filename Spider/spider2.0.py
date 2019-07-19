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

skipPicFlag = r'timg?'
def downloadPictures(url, save_path):
    # regex = r'src="(http.+?\.jpg)"'
    regex = r'src="(http[^ ]+?\.jpg)" '
    regexImg = re.compile(regex)
    imgList = regexImg.findall(getHtmlStr(url))

    n = 0
    for img in imgList:
        if img.find(skipPicFlag) < 0:
            print('_%d_' % n, img)
            n += 1
        elif len(imgList) == 1:
            print(r'略过图片')

    if not os.path.exists(save_path):
            os.makedirs(save_path)

    x = 0
    for img in imgList:
        if img.find(skipPicFlag) < 0:
            urllib.request.urlretrieve(img, save_path + '%s.jpg' %x)
            x += 1

testUrl = r'http://tieba.baidu.com/p/1753935195'
testTiebaUrl = r'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A3%81%E7%BA%B8'
curFilePath = os.path.dirname(__file__)
saveFilePathTest = curFilePath + '/savedFiles/'

# downloadPictures(testUrl, saveFilePath)

def getPicture(save_path):
    print('\n\n' + '-' * 10, r'帖子图片抓取', '-' * 10)
    url = input(r'请输入某个帖子的url:')
    if url:
        print('-' * 10 ,r'开始抓取', '-' * 10)
        downloadPictures(url, save_path)
        print('-' * 10 ,r'下载成功', '-' * 10)
        os.system("explorer.exe %s" % os.path.realpath(save_path))
    else:
        pass

def getPicturesByPostID(save_path, max_download = 10, input_name_mode = False):
    print('\n\n' + '-' * 10, r'百度贴吧图片抓取', '-' * 10)
    regex = r'data-field=\'{&quot;id&quot;:(\d+?),' # data-field="{"id":(\d+?),|data-field=\'{&quot;id&quot;:(\d+?),
    regexPostID = re.compile(regex)

    if False == input_name_mode:
        url = input(r'请输入某个贴吧的url:')
    else:
        name = input(r'请输入某个贴吧的名字:')
        url = r'https://tieba.baidu.com/f?ie=utf-8&kw=' + name

    postIdList = regexPostID.findall(getHtmlStr(url))
    urlList = []
    
    # print(postIdList)
    for i in range(len(postIdList)):
        urlList.append(r'http://tieba.baidu.com/p/' + postIdList[i])
    # print(urlList)

    if not os.path.exists(os.path.realpath(save_path)):
        os.makedirs(os.path.realpath(save_path))

    if True == input_name_mode:
        print('↓'*10, name + '吧开始', '↓'*10)

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

    if True == input_name_mode:
        print('\n' + '↑'*10, name + '吧结束', '↑'*10)

    os.system("explorer.exe %s" % os.path.realpath(save_path))

if __name__ == "__main__":
    print(r'TiebaSpider2.0 by ybs@20190719')
    while True:
        saveFilePath = os.getcwd() + '/savedFiles/' + dt.datetime.now().strftime(r'%Y%m%d-%H%M%S/')
        choice = input('请输入要抓取的方式<1.帖子url，2.贴吧url，3.贴吧名字>：')
        choice = int(choice)

        if 1 == choice:
            getPicture(saveFilePath)
        elif 2 == choice:
            cnt = input('请输入本次最多希望抓取的帖子数：')
            if int(cnt) > 0:
                getPicturesByPostID(saveFilePath, int(cnt))
        elif 3 == choice:
            cnt = input('请输入本次最多希望抓取的帖子数：')
            if int(cnt) > 0:
                getPicturesByPostID(saveFilePath, int(cnt), True)

        if 'Y' != input('\n\n本次任务结束，是否继续<Y/N>：').upper():
            break
