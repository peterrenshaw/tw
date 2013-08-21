#!/usr/bin/env python
# ~*~ encoding: utf-8 ~*~


import sys
from optparse import OptionParser


import tw.tools


# main controller of code & cli logic
def main():
    """controller & guts of code, cli logic"""
    usage = "usage: %prog [-r -v -h] -s"
    parser = OptionParser(usage)
    parser.add_option("-r", "--report", dest="report", 
                      help="report last 'n' messages sent")                                  
    parser.add_option("-s", "--send", dest="send", 
                      help="send a message")              
    parser.add_option("-l", "--lyric", dest="lyric",
                      help="send a lyric message")         
    parser.add_option("-v", "--version", dest="version", \
                      action="store_true",
                      help="current version")    
    options, args = parser.parse_args()

    
    # --- configure options by commandline else default
    if options.version:
        print("%s v%s %s %s" % (tw.config.NAME, tw.config.VERSION, \
                                tw.config.DATE, tw.config.COPYRIGHT))
        sys.exit(0)
    if options.send:
        tw.tools.send(options.send)
    elif options.lyric:
        note = "♬"
        msg = "%s %s %s" % (note, options.lyric, note)
        status = tw.tools.send(msg)
        tw.tools.display(status)
    elif options.report:
        print("report '%s'" % options.report) 
    else:
        parser.print_help()   
 
if __name__ == "__main__":  
    main()

# vim: noet:noai:ts=4:sw=4:tw=78

