#!/usr/bin/python
#_*_coding:utf-8_*_
print('*' * 40)
print("1:苹果")
print("2:橘子")
print("3:西瓜")
print("4:退出")
print('*' * 40)
while True:
    fruits = int(input("输入水果编号："))
    price = float(input("请输入单价："))
    weight = float(input("请输入重量："))
    if fruits == 1:
        print("苹果的价格为:%.2f" %(price * weight))
    elif fruits == 2:
        print("橘子的价格为:%.2f" %(price * weight))
    elif fruits == 3:
        print("西瓜的价格为:%.2f" %(price * weight))
    elif fruits == 4:
        break
    else:
        print("没有你想要的水果")