# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 下午9:39
# @Author  : Zheng Xingtao
# @File    : z_02_列表.py


"""对列表不同操作进行性能测试"""

from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l += [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


"""通过 timeit 模块, 进行时间测试"""

t1 = Timer("test1", "from __main__ import test1")
print("concat", t1.timeit(number=1000), "millseconds")

t2 = Timer("test2", "from __main__ import test2")
print("append", t2.timeit(number=1000), "millseconds")

t3 = Timer("test3", "from __main__ import test3")
print("comprehension", t3.timeit(number=1000), "millseconds")

t4 = Timer("test4", "from __main__ import test4")
print("list range", t4.timeit(number=1000), "millseconds")

# Python 列表操作的大O效率


"""list pop操作的性能分析"""
popzero = Timer("x.pop(0)", "from __main import x")
popend = Timer("x.pop()", "from __main import x")

x = list(range(2000000))
popzero.timeit(number=1000)

x = list(range(2000000))
popend.timeit(number=1000)

"""pop(0) pop() 在不同列表长度下的性能"""
popzero = Timer("x.pop(0)", "from __main import x")
popend = Timer("x.pop()", "from __main import x")

print("pop(0) pop()")
for i in range(1000000, 1000001, 1000000):
    x = list(range(i))
    pt = popend.timeit(number=1000)

    x = list(range(i))
    pz = popzero.timeit(number=1000)

    print("%15.5f, %15.5f" % (pz, pt))
