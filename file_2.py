#!/usr/bin/python
#_*_coding:utf-8_*_
#成绩评选
score = int(input("plerse a num:"))
if score >= 90:
    print ("A")
    print ("very good")
elif score >= 80:
    print ("B")
    print ("good")
elif score >= 70:
    print ("C")
    print ("pass")
else:
    print ("D")
print ("END")