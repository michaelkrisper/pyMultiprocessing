#!/usr/bin/python3
# coding=utf-8
"""
Tutorial from https://www.youtube.com/watch?feature=player_detailpage&v=EvbA3qVMGaw#t=1190
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import threading
import time

lock = threading.Lock()

def timer(name, delay, repeat):
    print("Timer {} started.".format(name))
    lock.acquire()
    while repeat > 0:
        time.sleep(delay)
        print("{}: {}".format(name, str(time.ctime(time.time()))))
        repeat -= 1
    print("{} is releasing the lock.".format(name))
    lock.release()
    print("Timer {} completed.".format(name))


def main():
    t1 = threading.Thread(target=timer, args=("Timer1", 1, 5))
    t2 = threading.Thread(target=timer, args=("Timer2", 0.75, 10))

    t1.start()
    t2.start()

    print("Main Complete")


if __name__ == "__main__":
    main()