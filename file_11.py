#!/usr/bin/python
#_*_coding:utf-8_*_
#检查是否是纯数字
import sys
def isNum(s):
    for i in s:
        if i in "0123456789":
            pass
        else:
            print("不是纯数字")
            break
    else:
            print("是纯数字 ")


isNum(sys.argv[1])