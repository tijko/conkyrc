#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def parse_json(json_data, hdline):
    if isinstance(json_data, list):
        for i in json_data:
            hdline = parse_json(i, hdline)
    elif isinstance(json_data, dict):
        for k in json_data.keys():
            if k == 'linkText' and json_data[k] not in hdline:
                hdline.append(json_data[k])
            else:
                hdline = parse_json(json_data[k], hdline)
    return hdline

def sports_flash():
    key = "YOUR_KEY"
    req = requests.get('http://api.espn.com/v1/now/top?apikey=' + key)
    page_json = req.json()
    flash = parse_json(page_json, [])
    return flash

if __name__ == '__main__':
    print ' | '.join(i for i in sports_flash())
            
