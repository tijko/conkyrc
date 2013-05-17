#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import BeautifulSoup


def weather():
    soup = BeautifulSoup.BeautifulSoup(urllib2.urlopen('http://weather.yahoo.com').read())
    whole = soup.find('div',id='MediaWeatherObservation')
    condition = whole.find('li',{'class':'condition first'}).text
    right_now_temp = whole.find('div',{'class':'day-temp-current temp-f '}).text   
    forecast =  whole.find('div',id='detail-day-0').text
    return forecast 

if __name__ == '__main__':
    print weather()
