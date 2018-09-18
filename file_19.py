#!/usr/bin/python
#_*_coding:utf-8_*_
import string
import random




pwd = ''


all_choice = string.ascii_letters + string.digits

for i in range(8):
    pwd += random.choice(all_choice)

print(pwd)