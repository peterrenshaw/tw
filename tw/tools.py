#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

import os
import ast
import sys
import os.path
import datetime


import tw.twi


from tw.config import DISPLAY
from tw.config import FMT_yyyymmmdd

from tw.config import BATCH_DATA_LEN
from tw.config import BATCH_DATA_LINE
from tw.config import BATCH_KEY_STATUS
from tw.config import BATCH_KEY_MESSAGE
from tw.config import BATCH_FILEPATH_DIR
from tw.config import BATCH_FILENAME_EXT


from tw.config import SAVE_FILENAME_EXT


#--- Display ---
def display(message, is_on=DISPLAY):
    """debug & display messages"""
    if message and is_on:
        print(message)
    else:
        pass
#--- Display ---

#--- Misc ---
def message_status(msg, msg_max=140):
    """count messag and send back status and char left"""
    msg_count = len(msg)
    msg_count_left = msg_max - msg_count
    if msg_count <= msg_max:
        status = True
    else:
        status = False
    return status, msg_count, msg_count_left
def send(message):
    """send a message"""
    status, count, delta = message_status(message)
    if status: 
        t = tw.twi.Twi()
        if not t.send(message): 
            print("warning: problem sending message")
            sys.exit(1)
        else:
            t = None
            sys.exit(0)
    else:
        print("warning message is %s long and %d over" % (count, delta))
        print("\t'%s'" % message)
#--- Misc ---

#--- Time routines ---
def dt_new_filename(ext=BATCH_FILENAME_EXT, dt_fmt=FMT_yyyymmmdd):
    """create new batch filename from c urrent date with format FMT"""
    dt = datetime.datetime.now().strftime(dt_fmt).upper()
    if ext: 
        return "%s.%s" % (dt, ext)
    else:
        return dt
def dt_new_save_filename(ext=SAVE_FILENAME_EXT, dt_fmt=FMT_yyyymmmdd):
    """create new save json filename"""
    return dt_new_filename(ext, dt_fmt)
def dt_new_batch_filename(ext=BATCH_FILENAME_EXT, dt_fmt=FMT_yyyymmmdd):
    """create new batch txt filename"""
    return dt_new_filename(ext, dt_fmt)
#--- Time routines ---


# vim: noet:noai:ts=4:sw=4:tw=78
