#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 复制固件到固件发布路径，并对固件重命名，需确保源程序Start_PreInit()函数中使用#if 1 '

__author__ = 'bingshuizhilian'
__createdate__ = '20190915'



import os, shutil, json
from datetime import datetime
from ReadIcmBasicInfo import ReadIcmBasicInfo

SW_VERSION = ''
HW_VERSION = ''

SRC_FILE = '../Debug/Exe/testTraveo.srec'
DEST_FILE = '../firmware_release/Chery_model_sw_hw_dt.srec'



def DoReleaseFirmware(srcfile, destfile, addversioninfo = False):
    if not os.path.exists(os.path.split(DEST_FILE)[0]):
        os.makedirs(os.path.split(DEST_FILE)[0])
        
    try:
        dt = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        destfile = destfile.replace('dt', dt)

        if True == addversioninfo:
            destfile = destfile.replace('sw', 'sw' + SW_VERSION)
            destfile = destfile.replace('hw', 'hw' + HW_VERSION)
            
        shutil.copy(srcfile, destfile)
        print('保存成功')
    except Exception as e:
        print('保存失败：', e)   

if __name__ == "__main__":
    info = ReadIcmBasicInfo()
    SW_VERSION = info["software version"]
    HW_VERSION = info["hardware version"]
    model = info["model"]
    DEST_FILE = DEST_FILE.replace('model', model)
    DoReleaseFirmware(SRC_FILE, DEST_FILE, True)