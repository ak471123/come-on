#!/usr/bin/python
#_*_coding:utf-8_*_
#1.调用os模块
#2.输入创建路径
#3.创建

import os
path1 = input("请输入文件创建路径：")
path2 = input("请输入文件夹创建路径：")
f = open(path1,"w")
f.close()
os.mkdir(path2)