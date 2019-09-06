#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：7.fileprocess '

__author__ = 'bingshuizhilian'



import shutil

SRC_FILE = '7.fileprocess-sample.h'
FACTOR_STRING = ' * 9 / 10\n'

def ModifyWAVlengthForT1EProject(srcfile, makebkpfile = True):
    srcfilebkp = srcfile + '.orig'
    lines = []

    if True == makebkpfile: shutil.copy(srcfile, srcfilebkp)
    with open(srcfile, 'r', encoding='utf-8') as f: lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].find('WAV_') >= 0 and lines[i].find('_LEN') >= 0:
            lines[i] = lines[i][:-1] + FACTOR_STRING
    with open(srcfile, 'w', encoding='utf-8') as f: f.writelines(lines)

if __name__ == "__main__":
    ModifyWAVlengthForT1EProject(SRC_FILE)