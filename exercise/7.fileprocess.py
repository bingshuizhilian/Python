#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：7.fileprocess '

__author__ = 'bingshuizhilian'



FACTOR_STRING = '*9/10\n'
lines = []


if __name__ == "__main__":
    with open('7.fileprocess-sample.h', 'r', encoding='utf-8') as f1:
        lines = f1.readlines()
    
    for i in range(len(lines)):
        if lines[i].find('WAV_') >= 0 and lines[i].find('_LEN') >= 0:
            lines[i].rstrip('\n')
            lines[i] += FACTOR_STRING
            print(lines[i])

    with open('7.fileprocess-sample2.h', 'w', encoding='utf-8') as f2:
        f2.writelines(lines)