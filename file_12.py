#!/usr/bin/python
#_*_coding:utf-8_*_
#斐波那契
def fibs(num):
    fib = [0,1]
    for i in range(num - 2):
        fib.append(fib[-1] + fib[-2])
    return fib

#打印并调用
print(fibs(10))
print(fibs(20))


