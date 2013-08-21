#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

import os
import ast
import os.path
import datetime

import time
import random
from threading import Timer


from tw.config import DISPLAY
from tw.config import FMT_yyyymmmdd

from tw.config import BATCH_DATA_LEN
from tw.config import BATCH_DATA_LINE
from tw.config import BATCH_KEY_STATUS
from tw.config import BATCH_KEY_MESSAGE
from tw.config import BATCH_FILEPATH_DIR
from tw.config import BATCH_FILENAME_EXT


from tw.config import SAVE_FILENAME_EXT



def display(message, is_on=DISPLAY):
    """debug & display messages"""
    if message and is_on:
        print message
    else:
        pass

#--- Time routie ---
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

def helloworld(msg="hello world"):
    """sample function for t_timing"""
    if msg: print msg
    else: print "helloworld"

def t_timing(func, frequency, max_delay, is_delay_random):
    """
       timing function that repeats a 'function' of 'frequency'
       with 'delay'. Q: Is this thread safe if we reload from 
       another module?

       calling: 
                  t_timing(helloworld, 5, 10.0)

       func: any function you care to create. Note if you want to 
             pass arguments, pass them as actual arguments with the
             function & NOT as arguments with the function.
 
             eg: YES func(a,b,c) --> t_timing(func, a, b, c)
                 NO  func(a,b,c) --> t_timing(func(a,b,c))
                 
       frequency: the number of times to repeat (from 1)       
       delay: max delay in seconds as integer
       is_delay_random: T/F (false sets delay to constant delay in sec) 
    """
    print "func='%s' frequency='%s' max_delay='%s' is_delay_random='%s'" % (func, frequency, max_delay, is_delay_random)
    count = range(1, frequency)
    for c in count:
        t = Timer(0.0, func, args=[max_delay]).start()
        if is_delay_random:
            d = random.randint(1, max_delay)  # delay is random
        else:
            d = max_delay                     # delay is constant 
        time.sleep(d)
#--- time routines ---

#
# DO ONE THING AT A TIME
#
# count message in que
# pop a message
# extract ACTION, STATUS, MESSAGE
# send MESSAGE by ACTION
# update STATUS
# update TOTAL_COUNT
# if count = 0:
#     break with total count
# else
#     #continue
def b_process(messages):
    """
    process a batch of messages, one at a time using
    a timing loop. 

    args:
        messages: a list of messages
    """
    total = 0
    print "messages='%s'" % messages
    print "count=", len(messages)
    count = len(messages)
    if count > 0:
        total = total + 1
        m = messages.pop()    # pop a message off the stack
        action = m["action"]
        status = m["status"]
        message = m["message"]
        if action == 1:
            # send lyric
            print "send lyric '%s'" % message
        else:
            # send normal 
            print "send normal '%s'" % message

        # change current message status on file
        print "changing message status from '%s' to '%s'" % (0,1) 
    else:
        return total


def new_batch_create(filepath_name, batch_dir=BATCH_FILEPATH_DIR, \
                     batch_data_len=BATCH_DATA_LEN, \
                     batch_data=BATCH_DATA_LINE):
    """create new batch file"""
    fnp = os.path.join(batch_dir, filepath_name)
    f = open(fnp, "w")

    top = "# ~*~ encoding: utf-8 ~*~\n"
    body = "%s\n\n\n\n\n\n\n\n\n\n\n" % BATCH_DATA_LINE
    end = "# vim: noet:noai:ts=4:sw=4:tw=%s" % batch_data_len
    data = "%s%s%s" % (top, body, end)
    f.write(data)
    f.close
    return True
def load_batch_send(filepath_name):
    """load file with messages to send"""
    pass
def update_batch_send(mid, m_status, filepath_names):
    """update send status of line given message ID"""
    pass

def str_2_dict(s):
    """convert string to dictionary"""
    return ast.literal_eval(s)

def is_batch_line(line, line_valid=BATCH_DATA_LINE):
    """compare line to valid line"""
    keys = line.keys()
    keys_batch = line_valid.keys()
    if keys == keys_batch:
        return True
    else:
        return False

def get_batch(todays_date, ext=BATCH_FILENAME_EXT, \
                   batch_dir=BATCH_FILEPATH_DIR):
    """return list of batch messages"""
    batch = []
    fnt = "%s.%s" % (todays_date, ext)
    fnp = os.path.join(os.getcwd(), batch_dir, fnt)
    if os.path.isfile(fnp):
        f = open(fnp, 'r')
        d = f.read()
        f.close
        if d:
            contents = d.split("\n")
            for line in contents[1:]:
                if line: 
                    msg = str_2_dict(line)
                    batch.append(msg)
                else:
                    break

            return batch
        else:
            return batch
    else:
        return batch 

def is_batch_found(todays_date, ext=BATCH_FILENAME_EXT, \
                   batch_dir=BATCH_FILEPATH_DIR, \
                   bk_status=BATCH_KEY_STATUS, bk_message=BATCH_KEY_MESSAGE):
    """locate batch file for today, read contents return status"""
    fnt = "%s.%s" % (todays_date, ext)
    fnp = os.path.join(os.getcwd(), batch_dir, fnt)
    if os.path.isfile(fnp):
       # found, check if contents
       f = open(fnp, 'r')
       d = f.read()
       f.close
       if d: 
           contents = d.split("\n")
           line = str_2_dict(contents[1])
           # is first line valid?
           if is_batch_line(line): 
               return True
           else:
               return False
       else:
           return False
    else:
        return False

# vim: noet:noai:ts=4:sw=4:tw=78
