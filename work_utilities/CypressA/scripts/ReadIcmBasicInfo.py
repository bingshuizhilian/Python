#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 读取软件版本号、硬件版本号、零件号 '

__author__ = 'bingshuizhilian'
__createdate__ = '20191005'



import json

INFO_FILE = './midwares/icmbasicinfo.json'

def ReadIcmBasicInfo(infofile = INFO_FILE):
    with open(infofile, 'r', encoding='utf-8') as f:
        info = json.load(f)
        return info

if __name__ == "__main__":
    print(ReadIcmBasicInfo())