#!/usr/bin/python3
# coding=utf-8
"""
Tutorial from https://www.youtube.com/watch?v=EvbA3qVMGaw#t=708
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"

import threading
import time


class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        with open(self.out, "a") as f:
            f.write(self.text)
        time.sleep(2)
        print("Finished background file write to {}".format(self.out))


def main():
    message = input("Enter a message: ")
    background = AsyncWrite(message, "out.txt")
    background.start()
    print("Main finished.")


if __name__ == "__main__":
    main()