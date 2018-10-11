#!/usr/bin/python
#_*_coding:utf-8_*_
#1.调用random和string模块
#2.定义变量和密码库
#3.利用循环随机打出8位密码
import random
import string
pwd = ''
all_choice = string.ascii_letters + string.digits
for i in range(8):
    pwd += random.choice(all_choice)
print(pwd)

