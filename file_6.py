#!/usr/bin/python
#_*_coding:utf-8_*_
#检查进站
ticket = int(input("请输入是否有票："))
l = int(input("请输入刀具长度："))
if ticket == 1:
    print("你有票可以进站！")
    # if knife == 1:
    #     print("你有刀具需要检查")
    # else:
    #     print("你可以进站！")
    if l > 10:
        print("刀具太长，拒绝进站！")
    else:
        print("您可以进站！")
else:
    print("先买票在进站！")