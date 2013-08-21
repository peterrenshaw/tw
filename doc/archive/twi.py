#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


from __future__ import with_statement


import os
import sys
import time
import codecs
import datetime


import tweepy
import tw.config


from tw.config import FILEPATH_SENT

from tw.tools import display
from tw.tools import dt_new_save_filename

def send_lyric(msg):
    """send lyrical tweet message to twitter"""
    m = u""
    m = "%s %s %s" % (tw.config.DECORATE_SONG, msg, tw.config.DECORATE_SONG)
    return send(m)
def send(msg):
    """send tweet message to twitter"""
    t = Twi()
    display("sending <%s>" % msg) 
    if t.send(msg):
        t = None
        return True
    else:
        t = None
        print "Error: problem sending message\n\t'%s'" % (msg)
        return False

class Twi:
    """thin wrapper around tweepy to send, save and other nice things"""
    def __init__(self, \
                 consumer_key=tw.config.CONSUMER_KEY, \
                 consumer_secret=tw.config.CONSUMER_SECRET, \
                 access_key=tw.config.ACCESS_KEY, \
                 access_secret=tw.config.ACCESS_SECRET ):
        """setup twi"""
        if not (consumer_key or consumer_secret or access_key or access_secret):
            print "Error: verification details are not valid. Fix them!"    
            sys.exit(1)
                      
        self.api = None
        self.authenticate(consumer_key, consumer_secret, \
                           access_key, access_secret)
        
    def authenticate(self, consumer_key, consumer_secret, \
                           access_key, access_secret):
        """
        connect to twitter using oauth. success will mena tweepy 
        has access to api.
        """
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_key, access_secret)
            self.api = tweepy.API(auth)
            display("api = %s" % self.api)
            display("connected")
        except tweepy.error.TweepError, e: #tweepy.TweepError:
            print "Error: We have a connection problem and cannot authenticate"
            print "%s" % tweepy.TweepError
            print e
            auth = None 
            self.api = None
            sys.exit(1)
        
        return True
    def send(self, message, is_lyric=False):
        """message sent to twitter"""
        message = u"%s" % message
        if self.valid(message):
            display("sending message")
            try:
                # nice hack by TomPerry a bug caused by twitter
                # https://dev.twitter.com/discussions/12107
                update = self.api.update_status(status=message, headers={'content-length': 0})
                self.save(message, update)
                print "send message\n%s" % message 
            except tweepy.error.TweepError, e: #tweepy.TweepError:
                print "Error: We have a connection problem and cannot authenticate"
                print "%s" % tweepy.TweepError
                print e
                self.api = None
                sys.exit(1)
            return True   
        else:
            return False 
    def save(self, message, update):
        """cache the message"""
        display("saving message")
        display("message = %s" % message)
        display("update.text = %s" % update.text)
        display("update = %s" % update.id)
        
        fn = dt_new_save_filename()
        fp = os.path.join(os.getcwd(), FILEPATH_SENT)

        if not os.path.isdir(fp):
            print "Error: can't save, invalid filepath"
            print "fp = '%s'" % fp
            sys.exit(1)
        fpn = os.path.join(fp, fn)
            
        with open(fpn, 'a') as f:
            t = time.mktime(datetime.datetime.now().timetuple())
            line = u""
            line = """{"message": "%s","status": "%s","date": %s}\n""" %  (message, update.id, t)
            print "line:\n\t<%s>" % line
            f.write(line)
        display("message saved")
        
        return True       
    def valid(self, message):
        """check if we can send a message"""
        display("checking message")
        if self.api:
            len_msg = len(message)
            display("message count = %s" % len(message))
            if len_msg > 0 and len_msg <= 140:
                return True
            else:
                print "%s" % len_msg
                return False
        else:
            return False      


# vim: noet:noai:ts=4:sw=4:tw=78
