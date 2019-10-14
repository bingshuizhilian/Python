#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 分割二进制文件 '

__author__ = 'bingshuizhilian'
__createdate__ = '20191006'



import sys

ORIG_BINARY_FILE = 'image.bin'
OUTPUT_BINARY_FILE = 'output.bin'
DIVIDE_FACTOR = 32 * 512
PADDIND_BYTES = b'\xff' * 512



def ProcessBinaryFile(binfile = ORIG_BINARY_FILE, outfile = OUTPUT_BINARY_FILE):
    origBinFile = []
    with open(binfile, 'rb') as fr:
        origBinFile = fr.read()

    bufferedBinFile = [origBinFile[i:i+DIVIDE_FACTOR] for i in range(0, len(origBinFile), DIVIDE_FACTOR)]

    if len(bufferedBinFile[-1]) < DIVIDE_FACTOR:
        bufferedBinFile[-1] += b'\xff' * (DIVIDE_FACTOR - len(bufferedBinFile[-1]))

    with open(outfile, 'wb') as fw:
        for i in bufferedBinFile:
            fw.write(i)
            fw.write(PADDIND_BYTES)



if __name__ == "__main__":
    try:
        if 3 == len(sys.argv):
            ProcessBinaryFile(sys.argv[1], sys.argv[2])
        else:
            ProcessBinaryFile()
    except Exception as e:
        print(e)
        print('\nusage: ProcessBinaryFile.exe [infilepath, outfilepath]')
        print('\nmail to bingshuizhilian@yeah.net for any question')
        input('\npress any key to exit')
