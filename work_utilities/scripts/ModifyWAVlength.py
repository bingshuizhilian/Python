#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' T1E的WAV音频长度需要在现有基础上乘以固定因子(9/10)，否则播放到最后时会有一声异响 '

__author__ = 'bingshuizhilian'
__createdate__ = '20190906'



import shutil

SRC_FILE = '../src/task/Graphics/image_address.h'
FACTOR_STRING = ' * 9 / 10\n'

def ModifyWAVlength(srcfile, makebkpfile = True):
    srcfilebkp = srcfile + '.orig'
    lines = []
    isalreadycatched = False

    with open(srcfile, 'r', encoding='utf-8') as f: lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].find('WAV_') >= 0 and lines[i].find('_LEN') >= 0:
            if lines[i].find(FACTOR_STRING) >= 0:
                isalreadycatched = True
                break
            lines[i] = lines[i][:-1] + FACTOR_STRING
    
    if False == isalreadycatched:
        if True == makebkpfile: shutil.copy(srcfile, srcfilebkp)
        with open(srcfile, 'w', encoding='utf-8') as f: f.writelines(lines)
        print('已处理')
    else:
        print('未处理，因为待修改文件已经包含系数({})了'.format(FACTOR_STRING.strip()))

if __name__ == "__main__":
    ModifyWAVlength(SRC_FILE)