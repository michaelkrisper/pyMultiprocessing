#!/usr/bin/python3
# coding=utf-8

import timeit
import multiprocessing

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__updated__ = "2014-11-03"
__python_version__ = "3.4.1"

def f(iterable):
    num = 1
    for i in iterable:
        num += i
    return num

def test():
    f(range(100000))

def test2():
    step = 100000 // 8
    with multiprocessing.Pool(processes=4) as pool:
       pool.map(f, [range(x*step, (x+1)*step) for x in range(8)])


if __name__ == "__main__":
    print(timeit.timeit("test()", number=100, setup="from __main__ import test2,test"))
    print(timeit.timeit("test2()", number=100, setup="from __main__ import test2,test"))