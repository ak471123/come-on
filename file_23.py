#!/usr/bin/python
#_*_coding:utf-8_*_

#类的应用一
class Dog:
    def __init__(self):
        self.name = 'huahua'
        self.leg = 4
        self.age = 3
        self.color = 'bai'
    def show(self):
        print("name:%s，leg：%s，age：%s，color：%s" %(self.name,self.leg,self.age,self.color))


dog1 = Dog()

dog1.show()


#############################################################################

#类的应用er
class Dog:
    def __init__(self,names,legs,ages,colors):
        self.name = names
        self.leg = legs
        self.age = ages
        self.color = colors
    def show(self):
        print("name:%s，leg：%s，age：%s，color：%s" %(self.name,self.leg,self.age,self.color))


dog1 = Dog("dahuang","4","4","huang")

dog1.show()