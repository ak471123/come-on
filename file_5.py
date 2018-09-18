#!/usr/bin/python
#_*_coding:utf-8_*_
#选择
y = input("please choose [YES |NO | y | n | Y | N]:")

yn = y.lower()

if yn == 'y' or yn =='yes':
    print("1")
elif yn == 'n' or yn == 'no':
    print("2")
else:
    print("please choose [YES |NO | y | n | Y | N]:")