#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


import time
import random
from threading import Timer

def print_time():
    print "From print_time", time.time()

def print_some_times():
    print time.time()
    Timer(5, print_time, ()).start()
    Timer(10, print_time, ()).start()
    time.sleep(11)  # sleep while time-delay events execute
    print time.time()


def hello(delta):
    print "hello, world %ss" % (delta)

def timing(func, frequency, delay):
    count = range(1, frequency)
    
    for c in count:
        t = Timer(0.0, func, args=[delay]).start()
        delay = random.randint(1, 20)
        time.sleep(delay)
    
if __name__ == "__main__":
    #print_some_times()
    timing(hello, 5, 10.0)

# vim: noet:noai:ts=4:sw=4:tw=78
