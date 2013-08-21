#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


from __future__ import with_statement


import os
import sys
import time
import datetime


import tweepy
import tw.config


DISPLAY = tw.config.DISPLAY


def display(message, is_on=DISPLAY):
    """debug & display messages"""
    if message and is_on:
        print(message)
    else:
        pass

class Twi:
    """thin wrapper around tweepy to send, save and other nice things"""
    def __init__(self, \
                 consumer_key=tw.config.CONSUMER_KEY, \
                 consumer_secret=tw.config.CONSUMER_SECRET, \
                 access_key=tw.config.ACCESS_KEY, \
                 access_secret=tw.config.ACCESS_SECRET ):
        """setup twi"""
        if not (consumer_key or consumer_secret or access_key or access_secret):
            print("Error: verification details are not valid. Fix them!")    
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
        except tweepy.TweepError:
            print("Error: We have a connection problem \
                   and cannot authenticate")
            print("%s" % tweepy.TweepError)
            print("%s" % dir(tweepy.TweepError))
            auth = None 
            self.api = None
            sys.exit(1)
        
        return True
    def send(self, message):
        """message sent to twitter"""
        if self.valid(message):
            display("sending message")
            try:
                update = self.api.update_status(status=message)
                self.save(message, update)
            except tweepy.TweepError:
                print("Error: We have a connection problem and \
                       cannot authenticate")
                print("%s" % tweepy.TweepError)                
                self.api = None
                sys.exit(1)
            return True   
        else:
            return False 
    def save(self, message, update):
        """cache the message"""
        display("saving message")
        display("message = %s" % update.text)
        display("update = %s" % update.id)
        
        fn = "%s.json" % datetime.datetime.now().strftime("%Y%b%d").upper()
        fp = os.path.join(os.getcwd(), "data")

        if not os.path.isdir(fp):
            print("Error: can't save, invalid filepath")
            print("fp = '%s'" % fp)
            sys.exit(1)
        fpn = os.path.join(fp, fn)
            
        with open(fpn, 'a') as f:
            t = datetime.datetime.now()
            line = """{"message": "%s","status": "%s","date": %s}\n""" % (message, update.id, time.mktime(t.timetuple())) 
            f.write(line) 
        display("message saved")
        
        return True       
    def valid(self, message):
        """check if we can send a message"""
        display("checking message")
        if self.api: 
            display("message count = %s" % len(message))
            if len(message) > 0 and len(message) <= 140:
                return True
            else:
                return False
        else:
            return False      


# vim: noet:noai:ts=4:sw=4:tw=78
