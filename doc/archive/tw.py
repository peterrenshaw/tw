#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


import sys
from optparse import OptionParser


import tw.twi
import tw.tools
import tw.config

from tw.tools import get_batch
from tw.tools import is_batch_found
from tw.tools import new_batch_create
from tw.tools import dt_new_batch_filename
from tw.config import BATCH_FILENAME_EXT




# main controller of code & cli logic
def main():
    """controller & guts of code, cli logic"""
    usage = "usage: %prog [-t -r -v -h] -s -l"
    parser = OptionParser(usage)
    parser.add_option("-r", "--report", dest="report", 
                      help="report last 'n' messages sent")                       
    parser.add_option("-t", "--test", dest="test", 
                      help="test sending a message")                  
    parser.add_option("-s", "--send", dest="send", 
                      help="send a message")
    parser.add_option("-l", "--lyric", dest="lyric",
                      help="lyrics")
    parser.add_option("-b", "--batch", dest="batch",
                      action="store_true",
                      help="send batch of tweets from file")                       
    parser.add_option("-v", "--version", dest="version",
                      action="store_true",
                      help="current version")    
    options, args = parser.parse_args()

    
    # --- configure options by commandline else default
    if options.version:
        print "%s v%s %s %s" % (tw.config.NAME, tw.config.VERSION, \
                                tw.config.DATE, tw.config.COPYRIGHT)
        sys.exit(0)
    elif options.lyric:
        msg = u""
        msg = "%s %s %s" % (tw.config.DECORATE_SONG, options.lyric, \
                            tw.config.DECORATE_SONG)
        if tw.twi.send(msg): 
            sys.exit(0)
        else:
            sys.exit(1)
    elif options.batch:
        todays_date = tw.tools.dt_new_batch_filename(ext="") # sans ext
        if is_batch_found(todays_date):
            # what to do?
            # read lines till line empty
            # pop onto list
            # start timer
            # every N random timer ticks
            #     send post
            #     save data to original file, set BATCH_DATA_LINE.status from
            #     STATUS_MSG_WAIT to STATUS_MSG_SENT if valid. If not set to 
            #     STATUS_MSG_ERROR
            messages = []
            messages = get_batch(todays_date)
            print "m='%s'" %  messages
            if messages:
                for msg in messages:
                    print "m=%s" % msg
            else:
                print "no messages found"
        else:
            bfn = "%s.%s" % (todays_date, BATCH_FILENAME_EXT)
            if new_batch_create(bfn):
                print "new batch file created & ready to edit\n\t<%s>" % bfn 
            else:
                print "Error: cant create new batch file\n\t<%s>" % bfn 
                sys.exit(1)    
    elif options.send:
        t = tw.twi.Twi()
        msg = u""
        msg = options.send
        if tw.twi.send(msg): 
            sys.exit(0)
        else:
            sys.exit(1)
    elif options.test:
        print "test"
    elif options.report:
        print "report '%s'" % options.report 
    else:
        parser.print_help()   
 
if __name__ == "__main__":  
    main()

# vim: noet:noai:ts=4:sw=4:tw=78

