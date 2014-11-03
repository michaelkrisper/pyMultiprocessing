#!/usr/bin/python3
# coding=utf-8
"""
Semaphore Demo
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import threading
import time

sem = threading.Semaphore(2)

def timer(name, delay, repeat):
    print("Timer {} started.".format(name))
    sem.acquire()
    while repeat > 0:
        time.sleep(delay)
        print("{}: {}".format(name, str(time.ctime(time.time()))))
        repeat -= 1
    print("{} is releasing the lock.".format(name))
    sem.release()
    print("Timer {} completed.".format(name))


def main():
    t1 = threading.Thread(target=timer, args=("Timer 1 ", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer 2 ", 0.75, 10))
    t3 = threading.Thread(target=timer, args=("Timer 3 ", 2, 5))
    t4 = threading.Thread(target=timer, args=("Timer 4 ", 0.1, 3))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    print("Main Complete")


if __name__ == "__main__":
    main()