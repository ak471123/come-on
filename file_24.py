#!/usr/bin/python
#_*_coding:utf-8_*_

class SiZe:
    def __init__(self,num1,num2):
        self.x = num1
        self.y = num2
        # self.he = 0
        # self.cha = 0
    def sum(self):
        return "%s + %s = %s" %(self.x,self.y,self.x + self.y)
    def sub(self):
        return "%s - %s = %s" % (self.x, self.y, self.x - self.y)

    def suc(self):
        return "%s * %s = %s" % (self.x, self.y, self.x * self.y)

    def sud(self):
        return "%s / %s = %.0f" % (self.x, self.y, self.x / self.y)


ceshi = SiZe(9,1)
print(ceshi.sum())
print(ceshi.sub())
print(ceshi.suc())
print(ceshi.sud())