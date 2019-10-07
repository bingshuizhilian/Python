#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 复制固件到固件发布路径，并对固件重命名，需确保源程序Start_PreInit()函数中使用#if 1 '

__author__ = 'bingshuizhilian'
__createdate__ = '20190915'



import os, shutil, json
from datetime import datetime
from ReadIcmBasicInfo import ReadIcmBasicInfo



SRC_FILE = '../Debug/Exe/testTraveo.srec'
DEST_FILE = '../firmware_release/CheryT1E_HC_sw_hw_dt.srec'



def DoReleaseFirmware(srcfile, destfile, swver, hwver, addversioninfo = False):
    if not os.path.exists(os.path.split(destfile)[0]):
        os.makedirs(os.path.split(destfile)[0])
        
    try:
        dt = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        destfile = destfile.replace('dt', dt)

        if True == addversioninfo:
            destfile = destfile.replace('sw', 'sw' + swver)
            destfile = destfile.replace('hw', 'hw' + hwver)
            
        shutil.copy(srcfile, destfile)
        print('保存成功')
    except Exception as e:
        print('保存失败：', e)   

if __name__ == "__main__":
    info = ReadIcmBasicInfo()
    swv = info["software version"]
    hwv = info["hardware version"]
    DoReleaseFirmware(SRC_FILE, DEST_FILE, swv, hwv, True)
    