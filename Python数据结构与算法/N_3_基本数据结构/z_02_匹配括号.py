# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午8:56
# @Author  : Zheng Xingtao
# @File    : z_02_匹配括号.py

from pythonds.basic import Stack


def parse_checker_one(symbolString):
    """
    (()())()((()))
    通过读取符号, 第一次遇到--写入栈中,第二次遇到--从栈中去除
    最后如果 所有符号匹配并且栈为空,说明每个符号都有相匹配的
    """
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":  # 如果当前的符号为(, 就会被压入栈中
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()  # 移除的元素一定是之前遇到的(

        index += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


###**********###

def matches(open, close):
    """检测每一个从栈顶移除的符号是否与当前的右符号相匹配"""
    opens = "([{"
    closes = ")]}"

    return opens.index(open) == closes.index(close)


def parse_checker_two(symolString):
    """与one的区别在于: 当出现)]}时,必须检测其类型是否与栈顶的左符号类型相匹配"""
    s = Stack()
    balanced = True
    index = 0

    while index < len(symolString) and balanced:
        symol = symolString[index]
        if symol in "([{":
            s.push(symol)
        else:
            if s.isEmpty():
                balabced = False
            else:
                top = s.pop()
                if not matches(top, symol): # 改动的部分==> 添加了matches()
                    balabced = False
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False
