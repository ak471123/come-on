#!/usr/bin/python
#_*_coding:utf-8_*_

import os
proc_list = []
def isNum(s):
    for i in s:
        if i in "0123456789":
            pass
        else:
            return False
            break
    else:
        print(s)
        return True
counter = 0
for i in os.listdir("/proc"):
    #counter = 0
    if isNum(i):
        counter += 1
print(counter)