# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午9:31
# @Author  : Zheng Xingtao
# @File    : z_03_十进制数转换.py

from pythonds.basic import Stack


# "除以2"算法 -- 将十进制书转换成二进制数
def divideBy2(decNubmer):
    remstack = Stack()

    while decNubmer > 0:
        rem = decNubmer % 2  # 取余
        remstack.push(rem)
        decNubmer = decNubmer // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString
