# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 12:47:38 2018

@author: Hully
"""

import textwrap


    
filepath = ("C:/Users/Hully/Desktop/Python_f/newtext.txt")

# open de file
with open(filepath) as t:
    file_data = t.read()

#wrap the text
texto = textwrap.wrap(file_data, width=40)

#print each line
for element in texto:
    print(element)
    


