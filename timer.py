#!/usr/bin/python3
# coding=utf-8
"""
Tutorial from https://www.youtube.com/watch?v=EvbA3qVMGaw
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

from threading import Thread
import time


def timer(name, delay, repeat):
    print("Timer {} started.".format(name))
    while repeat > 0:
        time.sleep(delay)
        print("{}: {}".format(name, str(time.ctime(time.time()))))
        repeat -= 1
    print("Timer {} completed.".format(name))


def main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 0.75, 10))

    t1.start()
    t2.start()

    print("Main Complete")


if __name__ == "__main__":
    main()