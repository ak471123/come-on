#!/usr/bin/python
#_*_coding:utf-8_*_
#石头剪刀布小游戏
import random

all_choice = ['石头','剪刀','布']

win_list = ['石头','剪刀'],['剪刀','布'],['布','石头']

prompt = """(0)'石头'
(1)'剪刀'
(2)'布'
choose(0/1/2):"""
cwin = 0
pwin = 0

while cwin <2 and pwin <2:

    index = int(input(prompt))

    while index >=3:
        index = int(input(prompt))

    player = all_choice[index]

    computer = random.choice(all_choice)

    print("player:%s,computer:%s" %(player,computer))

    if player == computer:
        pass#print("\033[32;43;1mping\033[0m")
    elif [player,computer] in win_list:
        #print("\033[33;45;1mying\033[0m")
        pwin += 1
    else:
        #print("\033[34;43;1mshu\033[0m")
        cwin += 1
if pwin == 2:
    print("you win")
else:
    print("you lose")