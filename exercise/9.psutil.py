#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' exercise name：9.psutil.py '

__author__ = 'bingshuizhilian'



from psutil import net_if_addrs


if __name__ == "__main__":
    # print(net_if_addrs())
    for k, v in net_if_addrs().items():
        print(v)
        for item in v:
            address = item[1]
            if "-" in address and len(address)==17:
                print(address)
            if "" == address:
                exit(0)
            else:
                print('run')

