   __           _ 
  / /__      __(_)
 / __/ | /| / / / 
/ /_ | |/ |/ / /  
\__/ |__/|__/_/ [1]  
                  


2013AUG21
* uses tweepy and has restriction of python2-6/7
  <https://github.com/tweepy/tweepy>

* readying to upload as github code
- licensing moving towards GPL3

* added
- .gitignore
- .requirements.txt
- twi/secrets.py for key/secret values (not uploaded)
- ABOUT.txt, auth.py


2013JUN12
* problems with authentication
- upgraded tweepy
- added display flag in tw/tools.py

2013JAN20
* have to rethink the list idea
- timing example in doc/ didn't work

2013JAN11
* desirable: pass previous lists as filename on -b option
- this is good because a created list might expire with the code
  you have

  ./tw.py -b testing.lst
* if there is no list & first time you create a list then re-run 
  but don't add items, throw message of zero items in list, repopulate

* back into coding

2012DEC10
* what happens to a batch that you didn't send or if you want to specify a 
  particular date? 
* for lyrics check that text is lower case

2012DEC02
* batch mode that sends more than 1 tweet & also has ability to send via file
* want to be able to read lines from file
- overcome limitations of CLI input, namely adding '$' to a line.

/// read above me

2012OCT28
* refactorised tw.py
- changed -l so only required & calls twi.send to process
- changed -s calls twi.send to process msg
* refactored twi.py 
- added 'def send(msg)' to simplify/reduce code
* fixed a bug introduced by Twitter
- details <https://dev.twitter.com/discussions/12107>
- fix by @tomp83 Tom Perry who suggested using 
  ".update_status('tweet text', headers={'content-length': 0})"
- found this in twi.py Twi.send, L 70

2011MAY31
* installed on puffy OpenBSD4.9
- working ok
* start to add more features
- get previous posts
- delete old post by Next/previous selection
- stats on tweets sent
- extract links from twits sent

2010APR20
* error on connection
- works ok but object not properly explaining error

    Error: We have a connection problem and cannot authenticate
    <class 'tweepy.error.TweepError'>

2011APR18
* tests
- check data dir there (hardcoded)
- test all imported modules are there
+ when I installed app from start had to also 
  import quite a few external modules: simplejson
  & tweepy.

2011APR12
* Observations
- after using this for a while I've noticed a few
  things to fix, build and idea for a port.
- some things I've noticed:
+ have trouble setting up cli args
+ send message but don't know until I've tried to 
  send message is too big
+ excessively long urls have to go to bit.ly to get
  compessed url
+ how do I know if I've re-tweeted?
+ if I make a mistake I have to go back & delete online then 
  go back to the data/*.json file & add redacted=true to the 
  data file


* Fix
- check for data dir if not in source dir
- create new data dir, warn user new dir is created & 
  save data
- notify user if new twits have been messaged to you
- re-load last N tweets so you can read past sent twits
- give user count of characters if failed to send

* Report
- want report of twits sent: OR read in twit as data to 
  be able to manipulate

* Port
- I want this ported to a webpage
+ use nodejs to call python backend

2011MAR27
* display
- added quick display method to allow turn off/on
* test 
- for test I should I use the test api? or just do as 
  I thought before (details of message/but not send)
* report
- turns tw.twi.DISPLAY to True
- allows all details to be shown for current message
- also read data/ files for more information stats

2011MAR26
* tw/data
- storage for json lines of twitter data sent. 
- stores the message, id and date in epoc format.
- lines are valid json but not as a whole file.
- filename is generated by YYYYMMMDD.json format.

* tw/config.py
- config options stored here 

* tw/twi.Twi
- object authenticates then allows to send a message, save
  and validate beforehand. 
- this has turned out the best way. Make sure you check the 
  except tweepy.TweepError examples and the API.

* tw.py 
- completed the command line for send & version. Yet to do test
  and report.
- should probably work on read, delete and a few other commands 
  to avoid having to check the site.

* tw/auth.py
- configuration: wrote a quick hack tw/auth.py which if you apply 
  for a dev consumer key/secret off twitter allows you to generate the 
  access key/secret to authenticate.

playing around with options. I want to be able to have the basics
like -v for version and -h for help. For sending I want to have
an option to send if valid <Send> (-s) and a test <Test> (-t) which 
allows you to play with input options that doesn't send but reports
the results. The last option is <Report> (-r) giving you stats on
the last "N" message sent including number of characters 

*options
-v = version
-s = send if ok
-t = tests if valid, reports msg actual & chopped, count
-r = last 'n' messasge sent

Originally I thought of:

-n = new is equiv to -d -s
-d = display only
-t = test & report
-s = test if count ok, send 
-c = count characters in post
-v = version

[1] 'Twi' title was created with an ASCII text generator using 'slant' and 'stretch=Yes". 
The code is based on Figlet which can be found here ~ <http://www.figlet.org/>
[Last accessed: Sunday 28th October, 2012]
<http://www.network-science.de/ascii/>

# vim: noet:noai:ts=4:sw=4:tw=78
