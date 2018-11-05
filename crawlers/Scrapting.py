

from bs4 import BeautifulSoup
import requests

# Abrir aqurivo em html
with open('C:\Users\Hully\Desktop\Python_f\reddit.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

print(soup.prettify())

""" Retorna um erro ao tentar abrir o arquivo em html"""

