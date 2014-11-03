#!/usr/bin/python3
# coding=utf-8
"""
Queue demo of producer consumer
https://docs.python.org/3.4/library/queue.html#module-queue
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import queue
import threading
import time

q = queue.Queue(3)

def producer(name, delay, repeat):
    print("Producer {} started.".format(name))
    for _ in range(repeat):
        time.sleep(delay)
        item = "{}: {}".format(name, str(time.ctime(time.time())))
        q.put(item)
        print("Producer {} produced item: {}".format(name, item))
    print("Producer {} completed.".format(name))


def consumer(name, delay, repeat):
    print("Consumer {} started".format(name))
    for _ in range(repeat):
        item = q.get()
        time.sleep(delay)
        print("Consumer {} got item: {}".format(name, item))
        q.task_done()
    print("Consumer {} completed.".format(name))


def main():
    t1 = threading.Thread(target=producer, args=(" 1 ", 1, 5))
    t2 = threading.Thread(target=producer, args=(" 2 ", 0.5, 5))
    t3 = threading.Thread(target=consumer, args=(" 1 ", 0.75, 10), daemon=True)
    t4 = threading.Thread(target=consumer, args=(" 2 ", 1.75, 10), daemon=True)

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    q.join()

    print("Main Complete")

if __name__ == "__main__":
    main()