#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from lxml import etree


def sunrise():
    req = requests.get('http://weather.yahooapis.com/forecastrss?w=2444445')
    data = etree.fromstring(req.content)
    for element in data.iter(
                         '{http://xml.weather.yahoo.com/ns/rss/1.0}astronomy'):
        return element.get('sunrise')

if __name__ == '__main__':
    sunup = sunrise()
    print ' ' + sunup
