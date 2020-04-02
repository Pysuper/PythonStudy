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
        binString += str(remstack.pop())

    return binString


# 将十进制数转换成任意进制数
def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"  # 创建一个数字字符串来存储对应位置上的数字 ==> 从栈中移除一个余数时，可用作访问数字的下标
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base  # "除以2" ==> "除以任意"

    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]

    return newString
