#!/usr/bin/python
#_*_coding:utf-8_*_

#导入有俩模块
import os,sys

def fun(path):
    isdir,isfile,join = os.path.isdir,os.path.isfile,os.path.join
    lsdir = os.listdir(path)

    dirs = [i for i in lsdir if isdir(join(path,i))]
    files = [i for i in lsdir if isfile(join(path,i))]

    if dirs:
        for d in dirs:
            fun(join(path,d))
    if files:
        for f in files:
            print(join(path,f))

fun(sys.argv[1])
