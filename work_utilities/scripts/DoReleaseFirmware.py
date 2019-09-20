#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 复制固件到固件发布路径，并对固件重命名，需确保源程序Start_PreInit()函数中使用#if 1 '

__author__ = 'bingshuizhilian'
__createdate__ = '20190915'



import os, shutil
from datetime import datetime

SRC_FILE = '../Debug/Exe/testTraveo.srec'
DEST_FILE = '../firmware_release/CheryT1E_HC_sw_hw_dt.srec'

SW_VERSION = '00.02.00'  # 软件版本号，仅影响生成的文件名，也可以后期直接在生成的文件名中修改
HW_VERSION = '0.0.9'     # 硬件版本号

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
    DoReleaseFirmware(SRC_FILE, DEST_FILE, True)