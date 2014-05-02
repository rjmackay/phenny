#!/usr/bin/env python
"""
ping.py - Phenny Hipchat Notification Module
Author: Sean B. Palmer, inamidst.com
About: http://inamidst.com/phenny/
"""

#import time
#import web
import urllib
#from tools import deprecated

def notification(phenny, input):
  def notify(phenny, input):
    link = ' https://api.hipchat.com/v1/rooms/message'

    message = input.sender + '/@' + input.nick + ': ' + input.group()
    query = {
      'from' : 'IRC',
      'message' : message,
      'auth_token' : phenny.config.hipchat_auth_code,
      'room_id' : phenny.config.hipchat_room_id,
      'message_format' : 'text'
    }

    u = urllib.urlopen(link, urllib.urlencode(query))
    response = u.read()
    code = u.getcode()

    if code != 200:
      print "Error: " + response
      return response

  try: notify(phenny, input)
  except Exception, e: print e
notification.rule = r'(.*)'
notification.priority = 'low'

if __name__ == '__main__':
   print __doc__.strip()