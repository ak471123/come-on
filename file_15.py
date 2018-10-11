#!/usr/bin/python
#_*_coding:utf-8_*_

import os
counter = 0
def isNum(s):
    for i in s:
        if i in "0123456789":
            pass
        else:
            break
    else:
        print(s)
        global counter
        counter + 1
for i in os.listdir("/proc"):
    if isNum(i):
        print(i)
print(counter)