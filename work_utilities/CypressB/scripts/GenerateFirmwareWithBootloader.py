#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 将bootloader固件与目标固件合成为一个固件，需确保源程序Start_PreInit()函数中使用#if 0 '

__author__ = 'bingshuizhilian'
__createdate__ = '20190918'



import os, json
from datetime import datetime
from copy import deepcopy
from ReadIcmBasicInfo import ReadIcmBasicInfo



PADDING_LINE = 'S31501A20000550101000000000000000000000000935D'

BOOT_FILE = './midwares/Bootloader.srec'
SRC_FILE = '../Debug/Exe/testTraveo.srec'
DEST_FILE = '../firmware_release/with_bootloader/CheryT1E_HC_sw_hw_withBootloader_dt.srec'



def GenerateFirmwareWithBootloader(bootfile, srcfile, destfile, swver, hwver, addversioninfo = False):
    if not os.path.exists(os.path.split(destfile)[0]):
        os.makedirs(os.path.split(destfile)[0])

    try:
        dt = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        destfile = destfile.replace('dt', dt)

        if True == addversioninfo:
            destfile = destfile.replace('sw', 'sw' + swver)
            destfile = destfile.replace('hw', 'hw' + hwver)

        bootReadBack = []
        bootDeepcopy = []
        with open(bootfile, 'r', encoding='utf-8') as bf:
            bootReadBack = bf.readlines()
            bootDeepcopy = deepcopy(bootReadBack)
            for line in bootReadBack:
                if line.upper().startswith('S7'):
                    bootDeepcopy.remove(line)

        srcReadBack = []
        srcDeepcopy = []
        with open(srcfile, 'r', encoding='utf-8') as sf:
            srcReadBack = sf.readlines()
            srcDeepcopy = deepcopy(srcReadBack)
            for line in srcReadBack:
                if line.upper().startswith(('S0', 'S315019F')):
                    srcDeepcopy.remove(line)

        with open(destfile, 'w', encoding='utf-8') as df:
            df.writelines(bootDeepcopy)
            df.write(PADDING_LINE + '\n')
            df.writelines(srcDeepcopy)

        print('合成成功')
    except Exception as e:
        print('合成失败：', e)   

if __name__ == "__main__":
    info = ReadIcmBasicInfo()
    swv = info["software version"]
    hwv = info["hardware version"]
    GenerateFirmwareWithBootloader(BOOT_FILE, SRC_FILE, DEST_FILE, swv, hwv, True)
