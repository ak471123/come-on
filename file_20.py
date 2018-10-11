#!/usr/bin/python
#_*_coding:utf-8_*_

import string,random,sys
def fun(num):
    pwd = ''
    all_choice = string.ascii_letters + string.digits

    for i in range(num):
        pwd += random.choice(all_choice)
    print(pwd)


if __name__ == '__main__':
    for i in range(int(sys.argv[2])):
        fun(int(sys.argv[1]))
