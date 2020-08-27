# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 14:46:17 2020

@author: QueenJ
"""


def get_web(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input("Address of web page: ")
content = get_web(url)
print(content)