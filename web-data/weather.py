#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree

def yahoo_weather():
    req = requests.get('http://weather.yahooapis.com/forecastrss?w=2444445')
    data = etree.fromstring(req.content)
    for element in data.iter(
                        '{http://xml.weather.yahoo.com/ns/rss/1.0}condition'):
        return ''.join([element.get('date'), ' ', 
                        element.get('text'), ' ', 
                        element.get('temp')])

if __name__ == '__main__':
    conditions = yahoo_weather()
    print conditions    
            
