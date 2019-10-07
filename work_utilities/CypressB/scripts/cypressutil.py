#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 集成py脚本到exe中 '

__author__ = 'bingshuizhilian'
__createdate__ = '20191006'



import sys
from DoReleaseFirmware import DoReleaseFirmware
from GenerateFirmwareWithBootloader import GenerateFirmwareWithBootloader
from GenerateApplicationFirmware import GenerateApplicationFirmware
from ModifyWAVlength import ModifyWAVlength
from ReadIcmBasicInfo import ReadIcmBasicInfo



def main():
    try:
        if sys.argv[1] == '-m':
            ModifyWAVlength(sys.argv[2])
        else:
            info = ReadIcmBasicInfo(sys.argv[2])
            swv = info["software version"]
            hwv = info["hardware version"]
            pn = info["part number"]

            if sys.argv[1] == '-r':
                DoReleaseFirmware(sys.argv[3], sys.argv[4], swv, hwv, True)
            elif sys.argv[1] == '-b':
                GenerateFirmwareWithBootloader(sys.argv[3], sys.argv[4], sys.argv[5], swv, hwv, True)
            elif sys.argv[1] == '-a':
                GenerateApplicationFirmware(sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], swv, hwv, pn, True)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    main()
