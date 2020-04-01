# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 下午8:48
# @Author  : Zheng Xingtao
# @File    : z_01_异序词检测.py

"""
对比不同方法实现 异序词检测 时的时间复杂度
异序词: 由相同字符构成的, 不是同一字符串的,两个字符串
"""


# 清点法
def anagramSolution1(s1, s2):
    """n^2/2 + n/2 ==> n^2 ==> O(n^2)"""
    alist = list(s2)
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 += 1

    return stillOK


# 排序法
def anagramSolution2(s1, s2):
    """排序操作起主导作用 ==> O(n^2) / O(nlogn)"""
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False
    return matches


# 蛮力法: 穷尽所有的可能
def anagramSolution3(s1, s2):
    """
    s1中的字符生成所有可能的字符串, 看s2时候在其中
    s1中字符生成的字符串总数为: n(n-1)(n-2)(n-3)...1 ==> n! (阶乘)
    20! = 2432902008176640000
    """
    pass


# 计数法
def anagramSolution4(s1, s2):
    """
    没有循环嵌套 ==> 2n+26 ==> n ==> 线性阶算法
    使用了计数器, 需要额外的空间 ==> 使用空间换来了时间
    """
    c1 = [0] * 26  # 实现两个计数器
    c2 = [0] * 26

    for i in range(len(s1)):  # 先数一下两个字符穿中，每个字符出现的次数
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1

    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False
    return stillOK


s1 = "qwe"
s2 = "wqe"
result = anagramSolution1(s1, s2)

print(result)
