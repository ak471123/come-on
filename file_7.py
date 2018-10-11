#!/usr/bin/python
#_*_coding:utf-8_*_
#计算1+。。。+100=？
sum = 0
for i in range(1,101):
    sum = sum + i
    print(sum)
#九九乘法
for i in range(1,10):
    for j in range(1,i+1):
        print("%s*%s=%s" % (j,i,j*i))
    print()
#斐波那契数列（总是前两个数之和）
fibs = [0,1]
for i in range(11):
    fibs.append(fibs[-1] + fibs[-2])
    print (fibs)
#for循环退出
import time
for  i in range(11):
    print(i)
   #time.sleep(1)
else:
    print('end')
#for循环退出控制break
for i in range(11):
    print(i)
    if i == 5:
        break
else:
    print('end')
#循环控制continue
for i in range(10):
    if i == 3:
        continue
    if i == 5:
        break
    print(i)
else:
    print('end')
