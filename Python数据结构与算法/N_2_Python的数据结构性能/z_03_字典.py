# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/1 下午9:39
# @Author  : Zheng Xingtao
# @File    : z_03_字典.py

"""对 字典 不同操作进行性能测试"""

# Python 字典操作的大O效率

"""比较列表和字典的包含操作"""
import timeit
import random

for i in range(10000, 1000001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    x = list(range(i))
    list_time = t.timeit(number=1000)

    x = {j: None for j in range(i)}
    dict_time = t.timeit(number=1000)

    print("%d, %10.3f, %10.3f" % (i, list_time, dict_time))
