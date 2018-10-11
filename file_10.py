#!/usr/bin/python
#_*_coding:utf-8_*_

#定义函数
def sun(x,y):
    return x + y

#传参方法一
# x = int(input("num1:"))
# y = int(input("num2:"))
#传参方法二
import sys

#解决异常
try:
# 应用模块（取值列表中元素位置）
    sun(int(sys.argv[1]),int(sys.argv[2]))
#print(sun(x,y))#调用函数
except TypeError as e:
    print(e,"请加入两个参数")