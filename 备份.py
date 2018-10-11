#!/usr/bin/python
#_*_coding:utf-8_*_
#备份思路
#1.打开备份文件
#2.读取内容
#3.创建一个新的文件
#4.将内容写入


f = open("/root/1.txt","r")
details = f.read()
b = open("/root/2.txt","w")
b.write(details)
f.close()
b.close()
print("备份完成")

##########################################################




