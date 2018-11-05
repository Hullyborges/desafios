# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 22:43:22 2018

@author: Hully
"""

from bs4 import BeautifulSoup
import requests


with open('C:\Users\Hully\Desktop\Python_f\reddit.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

print(soup.prettify())

