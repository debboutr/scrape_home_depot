# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:13:20 2018

@author: Rdebbout
"""
import re
import time
import random
import requests
import numpy as np
import pandas as pd
from ssl import SSLError
from bs4 import BeautifulSoup
from bs4.element import Tag
from selenium import webdriver
from requests import ConnectionError
from datetime import datetime
import pymysql.cursors



def strip_clean(text):
    return re.sub(r'\s+', ' ', text.replace('\n',''.strip()))

headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/69.0.3497.100 Safari/537.36')}


url = 'https://www.homedepot.com/c/site_map'
url = ('https://www.homedepot.com/p/Rust-Oleum-Specialty-29-oz-Countertop-'
       'Coating-Tint-Base-246068/202820906')

response  = requests.get(url, headers=headers)
response.status_code
data = response.text
soup = BeautifulSoup(data)
soup.findAll('<a>')
soup.find_all('a')
mydivs = soup.findAll("div", {"class": "content"})
a = mydivs[0]

col = a.find_all('a')
len(a.find_all('a'))
link = col[0]
type(link)
type(a)
type(soup)
link
soup.findParent
type(link.findParent()) # find if wrapped w/ <b> tag??
b = link.findParent()
b.get

count=0
grouped_urls = []
for anchor in mydivs:
    for link in anchor.find_all('a'):
        grouped = link.findParent().name != 'b'
        b_val = 'https://www.homedepot.com/b' in link['href']
        if grouped and b_val:
            print(link['href'])
            count += 1
            grouped_urls.append(link['href'])
len(col)

# =============================================================================
# above gets me all of the grouped urls from the sitemap w/o the header groups
# =============================================================================
amassed_urls = []
count = 0
for url in grouped_urls:
    count += 1
    print(count)
    response = requests.get(url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data)
    anchors = soup.find_all('a')
    for anchor in anchors:
        if not 'href' in anchor.attrs:
            continue
        if 'www.homedepot.com/b/' in anchor['href']:
#            pass
            amassed_urls.append(anchor['href'])
    
clean = list(set(amassed_urls))
clean2 = list(set(grouped_urls))
amassed_urls[:47]
    
    if soup.find("div",{'class':'page-header'}):
        filtered_urls = filtered_urls.append(url)
    if soup.find("h1",{'class':'page-header'}):
        soup.find_all('div',{'class':'grid'})




#https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class
#soup.findAll('div',
#             {'class': lambda x: x 
#                       and 'stylelistrow' in x.split()
#             }
#            )
        
               
url = 'https://www.homedepot.com/sitemap/d/plp_sitemap.xml'
response = requests.get(url, headers=headers)
data = response.text
soup = BeautifulSoup(data)
groups = soup.find_all('loc')
out = [group.text for group in groups]
comp = []
for url in out:
    response = requests.get(url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data)
    links = soup.find_all('loc')
    comp += [link.text for link in links]
        

p = list(set(comp))

len(p)    
p[:14]   
a = np.load('good_urls.npy').tolist()
b = np.load('good_urls2.npy').tolist()
c = np.load('good_urls3.npy').tolist()
d = np.load('good_urls4.npy').tolist()
e = np.load('good_urls5.npy').tolist()
f = np.load('good_urls6.npy').tolist()
g = np.load('good_urls7.npy').tolist()
h = np.load('good_urls8.npy').tolist()
total = np.load('unique_urls.npy').tolist()

p = np.load('good_urls9.npy').tolist()
total=list(set(a+b+c+d+e+f+g+h+i))
#☻
len(list(set(d)))
save = np.array(p)
#np.save('check_urls.npy',p)
np.save('nogos.npy',nogo)
# this gets everything under 232...
good_urls = []
len(list(set(good_urls)))
p[232]
p[3196]
p[13161]
p = p[232:]
p=p[19365]
#start at 13263 = 0
#first fail: 'https://www.homedepot.com/b/TheraPureSpa/N-5yc1vZbpp'
skips = []
count = 0
for url in p:
    count += 1
    print(count)
    current = url # keeps the original for indexing where we're at
    while url:
        if type(url) == Tag:
            print('~next!')
            url = f"https://www.homedepot.com{url['href']}"
        if url[:4] != 'http':
            url = f"https://www.homedepot.com{url}"
        try:
            response = requests.get(url, headers=headers)
        except UnicodeDecodeError:
            skips.append(url)
            break
        except ConnectionError:
            print('sleeping...ConnectionError')
            time.sleep(600)
            response = requests.get(url, headers=headers)
        except SSLError:
            print('sleeping...SSLError')
            time.sleep(600)
            response = requests.get(url, headers=headers)
        data = response.text
        soup = BeautifulSoup(data)
        git = soup.find("div", {"class": "mainContent"})
        if not git:
            break
        prods = git.find_all("a", {'data-pod-type': 'pr'})
        good_urls = good_urls + [prod['href'] for prod in prods]
        url = git.find('a', {'class':'hd-pagination__link','title':'Next'})
       

url
'https://www.homedepot.com/b/Decor-Wall-Decor-Mirrors-Wall-Mirrors/'
'Silver/N-5yc1vZ1z18fo4Z1z17yxz?Nao=336&Ns=None'
for x in range(4):
    git = 1
    if x == 2: 
        git = None    
    while git:
      
        print(x)

'https://www.homedepot.com/b/Plumbing-Plumbing-Accessories/N-5yc1vZbql8' in p




collect = [total.pop(total.index(t)) for t in total if t[:3] != '/p/']    
collect = [total.pop(total.index(t)) 
c2 = []
for t in total:
    if t[:3] != '/p/':
        c2.append(t)
        
rand = random.sample(total, 10)       
        
https://www.homedepot.com/p/Westinghouse-Tulsa-52-in-Indoor-Oil-Brushed-Bronze-Ceiling-Fan-7200600/205972717
https://www.homedepot.com/p/BEHR-MARQUEE-5-gal-MQ3-30-Petal-Tip-Semi-Gloss-Enamel-Interior-Paint-and-Primer-in-One-345005/207155990        
https://www.homedepot.com/p/Inoxia-SpeedTiles-Cairo-Beige-11-75-in-x-11-6-in-x-5-mm-Stone-Self-Adhesive-Mosaic-Wall-Tile-11-36-sq-ft-case-IS0210E217001L/303473997
https://www.homedepot.com/p/American-Standard-18293-0200-Renu-Brass-Tub-Shower-Stem-132433/205603862
https://www.homedepot.com/p/Daltile-Forest-Hills-Crema-18-in-x-18-in-Porcelain-Floor-and-Wall-Tile-360-sq-ft-pallet-FH011818HDPL1P6/302180680
https://www.homedepot.com/p/Pelican-Water-3-Stage-Whole-House-Water-Filtration-System-THD-PRL-3/207172271
https://www.homedepot.com/p/Creative-Gallery-16-in-x-20-in-Do-Something-Today-Acrylic-Wall-Art-Print-QOT61504A1620X/306583244


with open('open_home_depot_links_1.bat','w') as bat_file:
    for x in rand:
#        bat_file.write(f"start chrome.exe https://www.homedepot.com{x}\n")
        print(f"`https://www.homedepot.com{x}`")
        print('*'*50)
