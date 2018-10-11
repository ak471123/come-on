#!/usr/bin/python
#_*_coding:utf-8_*_

def wordCount(s):
    chars = len(s)
    words = len(s.split)
    lines = s.count('\n')
    print(lines,words,chars)
s = open("/etc/hosts").read()
if __name__ == '__main__':
    wordCount(s)