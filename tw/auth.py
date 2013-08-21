#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


import sys
import tweepy


import tw.config

#=
# name: auth.py
# date: 2011MAR26
# description:
#     a quick simple hack to get
#         - auth.access_token.key
#         - auth.access_token.secret
#     if you have your consumer_key & consumer_secret from 
#     twitter. 
#=
def main():
    print "start..."
    auth = tweepy.OAuthHandler(tw.config.CONSUMER_KEY, 
                                                         tw.config.CONSUMER_SECRET)
    print "auth, token, reqest"
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print "Error: Failed to get request token"
        sys.exit(1)
    print "url = %s" % redirect_url
    print "now copy the url and paste into browser"
    print "accept the request, copy the number"
    verifier = raw_input('Verifier:')
    auth.get_access_token(verifier)
    print "key = '%s'" % auth.access_token.key
    print "secret = '%s'" % auth.access_token.secret
        
if __name__ == '__main__':
    main()

# vim: noet:noai:ts=4:sw=4:tw=78

