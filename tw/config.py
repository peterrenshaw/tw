#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~

import secrets

NAME = "tw"
VERSION = "0.2.1"
DATE = "2013AUG21"
COPYRIGHT = "(C) 2010 - 2013"
DECORATE_SONG = u"♬"


DISPLAY = True
STATUS_MSG_ERROR = 0
STATUS_MSG_WAIT = 1
STATUS_MSG_SENT = 2
FMT_yyyymmmdd = "%Y%b%d"
FILEPATH_SENT = "data"
SAVE_FILENAME_EXT = "json"


# --- hack: hasn't worked yet ---
BATCH_FILENAME_EXT = "txt"
BATCH_FILEPATH_DIR = "batch"
BATCH_ACTION_TWEET = 0
BATCH_ACTION_MUSIC = 1
BATCH_DATA_LINE = {'action':BATCH_ACTION_TWEET, 'status':STATUS_MSG_WAIT, 'message':u''}
BATCH_DATA_LEN = len("{'action':0, 'status':1, 'message':u''}") + 140
BATCH_KEY_STATUS = "status"
BATCH_KEY_MESSAGE = "message"

TIMER_SEND_MIN = 15
TIMER_SEND_SEC = TIMER_SEND_MIN * 60 
# --- end hack ---

CONSUMER_KEY = secrets.CONSUMER_KEY
CONSUMER_SECRET = secrets.CONSUMER_SECRET
ACCESS_KEY = secrets.ACCESS_KEY
ACCESS_SECRET = secrets.ACCESS_SECRET


# vim: noet:noai:ts=4:sw=4:tw=78
