#!/usr/bin/env python
# -*- coding: utf-8 -*-

import poplib
import time
import simplejson


_addrs = {'gmail.com':'pop.gmail.com',
          'hotmail.com':'pop3.live.com',
          'aol.com':'pop.aol.com',
          'msn.com':'pop3.live.com',
          'live.com':'pop3.live.com'}

def email_check():
    emails = 0
    with open("") as f:
        acnts = f.read()
        acnts = simplejson.loads(acnts)
    for acnt in acnts:
        mail = acnt.split("@")[-1]
        session = poplib.POP3_SSL(_addrs[mail])
        if "gmail" in acnt:
            gmail = acnt.split("@")[0]
            session.user(gmail)
        else:
            session.user(acnt)
        session.pass_(acnts[acnt])
        emails += session.stat()[0]
        session.quit()
    return "You have %d new emails %s" % (emails, time.ctime())

if __name__ == '__main__':
    print email_check()        
