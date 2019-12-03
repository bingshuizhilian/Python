#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 从bootloader固件中提取flash driver文件 '

__author__ = 'bingshuizhilian'
__createdate__ = '20191025'



import os
from copy import deepcopy



BOOT_FILE = './midwares/Bootloader.srec'
DEST_FILE = './midwares/FlashDriver.srec'



def GenerateFlashDriverFile(bootfile, destfile):
    if not os.path.exists(bootfile):
        raise Exception('未检测到Bootloader.srec')

    if os.path.exists(destfile):
        os.remove(destfile)

    try:
        bootReadBack = []
        bootDeepcopy = []
        flashDriverFile = []
        with open(bootfile, 'r', encoding='utf-8') as bf:
            bootReadBack = bf.readlines()
            bootDeepcopy = deepcopy(bootReadBack)
            for line in bootReadBack:
                if line.upper().startswith('S315019F'):
                    bootDeepcopy.remove(line)
                elif line.upper().startswith('S7'):
                    flashDriverFile.append(line)

        flashDriverFile = bootDeepcopy[:33] + flashDriverFile

        with open(destfile, 'w', encoding='utf-8') as df:
            df.writelines(flashDriverFile)

        print('生成成功')
    except Exception as e:
        print('生成失败：', e)   

if __name__ == "__main__":
    GenerateFlashDriverFile(BOOT_FILE, DEST_FILE)
