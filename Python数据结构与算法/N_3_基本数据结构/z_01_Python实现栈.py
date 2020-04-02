# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/2 下午8:37
# @Author  : Zheng Xingtao
# @File    : z_01_Python实现栈.py

class StackEnd():
    """
    用Python实现栈 ==> 以列表的尾部作为栈的顶端
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class StackStart():
    """
    Python实现栈 ==> 以头部为栈的顶端
    注意: 用pop和insert, 显式的访问下标为0的元素
    """

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):   # 对栈进行存取操作时, 调整操作的位置
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

"""
两者的差异:
append()和pop()时间复杂度都是O(1) ==> 不论栈中有多少个元素，执行的时间是恒定的
insert(0)和pop(0)--O(n) ==> 执行时间随元素数量的增加而增加
"""