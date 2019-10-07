#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 将目标固件处理为可以通过bootloader加载的固件，需确保源程序Start_PreInit()函数中使用#if 0 '

__author__ = 'bingshuizhilian'
__createdate__ = '20190918'



import os, shutil, binascii, json
from datetime import datetime
from copy import deepcopy
from ReadIcmBasicInfo import ReadIcmBasicInfo

SW_VERSION = ''
HW_VERSION = ''
PART_NUMBER = ''

SRC_FILE = '../Debug/Exe/testTraveo.srec'
DEST_FILE = '../firmware_release/application_file/CheryT1E_HC_sw_hw_applicationFile_dt.srec'
SRC_FLASH_DRIVER_FILE = './midwares/FlashDriver.srec'
DEST_FLASH_DRIVER_FILE = '../firmware_release/application_file/CheryT1E_HC_flashDriverFile.srec'

crcLookupTable = (
    0x0000, 0x1021, 0x2042, 0x3063, 0x4084, 0x50A5, 0x60C6, 0x70E7,
    0x8108, 0x9129, 0xA14A, 0xB16B, 0xC18C, 0xD1AD, 0xE1CE, 0xF1EF,
    0x1231, 0x0210, 0x3273, 0x2252, 0x52B5, 0x4294, 0x72F7, 0x62D6,
    0x9339, 0x8318, 0xB37B, 0xA35A, 0xD3BD, 0xC39C, 0xF3FF, 0xE3DE,
    0x2462, 0x3443, 0x0420, 0x1401, 0x64E6, 0x74C7, 0x44A4, 0x5485,
    0xA56A, 0xB54B, 0x8528, 0x9509, 0xE5EE, 0xF5CF, 0xC5AC, 0xD58D,
    0x3653, 0x2672, 0x1611, 0x0630, 0x76D7, 0x66F6, 0x5695, 0x46B4,
    0xB75B, 0xA77A, 0x9719, 0x8738, 0xF7DF, 0xE7FE, 0xD79D, 0xC7BC,
    0x48C4, 0x58E5, 0x6886, 0x78A7, 0x0840, 0x1861, 0x2802, 0x3823,
    0xC9CC, 0xD9ED, 0xE98E, 0xF9AF, 0x8948, 0x9969, 0xA90A, 0xB92B,
    0x5AF5, 0x4AD4, 0x7AB7, 0x6A96, 0x1A71, 0x0A50, 0x3A33, 0x2A12,
    0xDBFD, 0xCBDC, 0xFBBF, 0xEB9E, 0x9B79, 0x8B58, 0xBB3B, 0xAB1A,
    0x6CA6, 0x7C87, 0x4CE4, 0x5CC5, 0x2C22, 0x3C03, 0x0C60, 0x1C41,
    0xEDAE, 0xFD8F, 0xCDEC, 0xDDCD, 0xAD2A, 0xBD0B, 0x8D68, 0x9D49,
    0x7E97, 0x6EB6, 0x5ED5, 0x4EF4, 0x3E13, 0x2E32, 0x1E51, 0x0E70,
    0xFF9F, 0xEFBE, 0xDFDD, 0xCFFC, 0xBF1B, 0xAF3A, 0x9F59, 0x8F78,
    0x9188, 0x81A9, 0xB1CA, 0xA1EB, 0xD10C, 0xC12D, 0xF14E, 0xE16F,
    0x1080, 0x00A1, 0x30C2, 0x20E3, 0x5004, 0x4025, 0x7046, 0x6067,
    0x83B9, 0x9398, 0xA3FB, 0xB3DA, 0xC33D, 0xD31C, 0xE37F, 0xF35E,
    0x02B1, 0x1290, 0x22F3, 0x32D2, 0x4235, 0x5214, 0x6277, 0x7256,
    0xB5EA, 0xA5CB, 0x95A8, 0x8589, 0xF56E, 0xE54F, 0xD52C, 0xC50D,
    0x34E2, 0x24C3, 0x14A0, 0x0481, 0x7466, 0x6447, 0x5424, 0x4405,
    0xA7DB, 0xB7FA, 0x8799, 0x97B8, 0xE75F, 0xF77E, 0xC71D, 0xD73C,
    0x26D3, 0x36F2, 0x0691, 0x16B0, 0x6657, 0x7676, 0x4615, 0x5634,
    0xD94C, 0xC96D, 0xF90E, 0xE92F, 0x99C8, 0x89E9, 0xB98A, 0xA9AB,
    0x5844, 0x4865, 0x7806, 0x6827, 0x18C0, 0x08E1, 0x3882, 0x28A3,
    0xCB7D, 0xDB5C, 0xEB3F, 0xFB1E, 0x8BF9, 0x9BD8, 0xABBB, 0xBB9A,
    0x4A75, 0x5A54, 0x6A37, 0x7A16, 0x0AF1, 0x1AD0, 0x2AB3, 0x3A92,
    0xFD2E, 0xED0F, 0xDD6C, 0xCD4D, 0xBDAA, 0xAD8B, 0x9DE8, 0x8DC9,
    0x7C26, 0x6C07, 0x5C64, 0x4C45, 0x3CA2, 0x2C83, 0x1CE0, 0x0CC1,
    0xEF1F, 0xFF3E, 0xCF5D, 0xDF7C, 0xAF9B, 0xBFBA, 0x8FD9, 0x9FF8,
    0x6E17, 0x7E36, 0x4E55, 0x5E74, 0x2E93, 0x3EB2, 0x0ED1, 0x1EF0
) # size: 256



def SplitHexString(s):
    return [s[i:i+2] for i in range(0, len(s), 2)]

def CalcCheckSum(s):
    datalist = [int(v, 16) for v in SplitHexString(s) if not v.startswith(('S', 's'))]
    ret = 0xff - sum(datalist) & 0xff
    ret = hex(ret).upper()[2:]
    if len(ret) < 2:
        ret = '0' + ret
    return ret

def CalcCRC16(l):
    payload = ''
    for line in l:
        if line.upper().startswith('S3'):
            payload += line.strip()[12:-2]

    if len(payload) % 2 != 0:
        raise Exception('不满足有效数据字节数一定是偶数的条件')

    datalist = [int(v, 16) for v in SplitHexString(payload)]
    crc16 = 0xffff
    tmp = 0
    for v in datalist:
        tmp = ((crc16 >> 8) & 0xff) ^ v
        crc16 = ((crc16 << 8) & 0xffff) ^ crcLookupTable[tmp]
    
    ret = hex(crc16).upper()[2:]
    if len(ret) < 4:
        ret = '0' * (4 - len(ret)) + ret
    return ret

def GenerateApplicationFirmware(srcfile, destfile, addversioninfo = False):
    if not os.path.exists(os.path.split(DEST_FILE)[0]):
        os.makedirs(os.path.split(DEST_FILE)[0])

    try:
        # 处理flash driver
        if os.path.exists(DEST_FLASH_DRIVER_FILE):
            os.remove(DEST_FLASH_DRIVER_FILE)
        shutil.copy(SRC_FLASH_DRIVER_FILE, DEST_FLASH_DRIVER_FILE)

        newflashdriverfile = []
        with open(DEST_FLASH_DRIVER_FILE, 'r', encoding='utf-8') as fdf:
            newflashdriverfile = fdf.readlines()
            
        partnumber = binascii.b2a_hex(PART_NUMBER.encode('utf-8')).decode('utf-8')
        newflashdriverfile[0] = 'S01900000747395957' + partnumber + '20' * (16 - len(partnumber) // 2) + '00'
        fds0checksum = CalcCheckSum(newflashdriverfile[0])
        newflashdriverfile[0] += fds0checksum + '\n'

        with open(DEST_FLASH_DRIVER_FILE, 'w', encoding='utf-8') as fdf:
            newflashdriverfile = fdf.writelines(newflashdriverfile)
        
        # 处理App
        dt = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        destfile = destfile.replace('dt', dt)

        if True == addversioninfo:
            destfile = destfile.replace('sw', 'sw' + SW_VERSION)
            destfile = destfile.replace('hw', 'hw' + HW_VERSION)

        srcReadBack = []
        appFile = []
        with open(srcfile, 'r', encoding='utf-8') as sf:
            srcReadBack = sf.readlines()
            appFile = deepcopy(srcReadBack)
            for line in srcReadBack:
                if line.upper().startswith(('S0', 'S315019F')):
                    appFile.remove(line)

        apps0line = 'S02100000747395957' + partnumber + '20' * (16 - len(partnumber) // 2) + '01'
        apps0line += binascii.b2a_hex(SW_VERSION.encode('utf-8')).decode('utf-8')
        apps0line += CalcCheckSum(apps0line) + '\n'
        appFile.insert(0, apps0line.upper())

        crc = CalcCRC16(appFile)
        crc = 'S31501A20000' + crc * 8
        crc += CalcCheckSum(crc) + '\n'
        appFile.insert(1, crc.upper())

        with open(destfile, 'w', encoding='utf-8') as df:
            df.writelines(appFile)

        print('合成成功')
    except Exception as e:
        print('合成失败：', e)   

if __name__ == "__main__":
    info = ReadIcmBasicInfo()
    SW_VERSION = info["software version"]
    HW_VERSION = info["hardware version"]
    PART_NUMBER = info["part number"]
    GenerateApplicationFirmware(SRC_FILE, DEST_FILE, addversioninfo = True)
