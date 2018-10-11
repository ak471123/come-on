#!/usr/bin/python
#_*_coding:utf-8_*_

class Dog:
    #使用了构造函数
    def __init__(self,names):
        self.name =names
    #
    def __str__(self):
        return"name is :%s" %(self.name)
dog1 = Dog("xiaohei")
print(dog1)