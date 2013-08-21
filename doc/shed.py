#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

import time
from threading import Timer
def print_time(msg):
    print "From print_time msg='%s'", time.time()

def print_some_times():
    print 'start'
    print time.time
    Timer(5, print_time('now and again'), ()).start()
    Timer(10, print_time('it works'), ()).start()
    time.sleep(11)  # sleep while time-delay events execute
    print time.time
    print 'end'

if __name__ == "__main__":
    print_some_times()


# vim: noet:noai:ts=4:sw=4:tw=78
