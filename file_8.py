#!/usr/bin/python
#_*_coding:utf-8_*_
#复制
s_file = '/usr/bin/ls'
d_file = '/home/sl'
buffer_size = 4096
s_obj_file = open(s_file,'rb')

d_obj_file = open(d_file,'wb')

while True:
    data = s_obj_file.read(buffer_size)
    if not data:
        break
    d_obj_file.write(data)
    s_obj_file.close()
    d_obj_file.close()