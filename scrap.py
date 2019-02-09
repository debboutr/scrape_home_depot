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


columns=['itemId','name','upc','categoryPath','shortDescription',
         'longDescription','brandName','thumbnailImage','mediumImage',
         'largeImage','size','color','modelNumber','productUrl',
         'customerRating','numReviews','offerType','datasheet_url']

tbl = pd.DataFrame(columns=columns)  

browser = webdriver.Chrome()

    
browser.quit()
 

urls = total[4700:]
web_no=1112029450
nogo = []
store = "Home Depot"

#problem
#https://www.homedepot.com/p/The-Company-Store-Velvet-Flannel-Wheat-Full-Fitted-Sheet-EU29-F-WHEAT/306531659
url = 'https://www.homedepot.com/p/BEHR-Premium-1-gal-PPU1-08-Pompeian-Red-Low-Lustre-Interior-Exterior-Porch-and-Patio-Floor-Paint-630001/302055334'

The BEHR Premium Porch and Patio Floor Paint Enamel is an interior and exterior floor coating for concrete and wood surfaces. This durable 100% acrylic latex finish resists mildew, scuffing, fading, cracking and peeling. Ideal for use on porches, floors, decks, basements and patios.
                        
                        
                        
for i, url in enumerate(urls):
    
    print(i)
    print (url)
    break
    url = f"https://www.homedepot.com{url}"
    response  = requests.get(url, headers=headers)
    data = response.text
    soup = BeautifulSoup(data)
    try:
        
        model_no = soup.find("h2", {"class": "product_details modelNo"})
        model_no = model_no.text.split('#')[-1].strip() if model_no else ''
        brand = soup.find("h2", {"class": "product-title__brand"})
        brand = brand.text.strip() if brand else ''
        # should I create a func for every .find() to make sure there is an object returned???
        title = soup.find("h1", {"class": "product-title__title"}).text.strip()
        image = soup.find("img", {"id": "mainImage"})['src']
        short = soup.find("meta", {"name": "description"})['content']
        desc = soup.find("p", {"itemprop": "description"}).text.replace('\n','').strip().replace('\'','')
     
        li = soup.find("div", {"class": "main_description"}).findAll("li")
        if li:
            desc = desc + '\n**' + '\n**'.join([strip_clean(x.text) for x in li])
        p = soup.find('div',{'id':'specsContainer'})
        hold={}
        tits = p.findAll('div',{'class':'specs__title'})
        tabs = p.findAll('div',{'class':'specs__table'})
        for tit, tab in zip(tits,tabs):
            second = {}
            for grp in tab.findAll('div',{'class':'specs__group'}):
                lbl = grp.findNext('div',{'class':'specs__cell--label'})
                cell = lbl.findNext('div',{'class':'specs__cell'})
                second[lbl.text] = cell.text
            hold[strip_clean(tit.text)] = second
        rating = soup.find("span", {"class": "bvseo-ratingValue"})
        rating = float(rating.text) if rating else 0
        num_reviews = soup.find("span", {"class": "bvseo-reviewCount"})
        num_reviews = int(num_reviews.text) if num_reviews else 0
    
        pdf_link = ''
        tags = soup.find("div", {"class": "info_guides"})
        if tags:
            tags = tags.findAll('a')
            for tag in tags:
                if 'SDS' in tag.text:
                   pdf_link = tag['href'] 
            
        browser.get(url)
        bread = browser.find_elements_by_class_name('breadcrumb__link')
        web_no += 1
        crumbs = '/'.join([crumb.text for crumb in bread])
        hay = ''
        for k,v in hold.items():
            hay += k + '\n'
            for i,j in v.items():
                hay += '  -' + i + ': ' + j +'\n' 
        hay = hay.replace('\'','') # remove ' chars cause it will fail on entering into DB
        desc = desc.replace('\'','')
    except:
        print('fail')
        nogo.append(url)
        continue
    connection = pymysql.connect(host='tesla.epa.gov',
                             user='rdebbout',
                             password='Donsende1',
                             db='prod_racp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = ("INSERT INTO products (itemId, "
                                           "name, "
                                           "categoryPath, "
                                           "shortDescription, "
                                           "longDescription, "
                                           "specifications, "
                                           "brandName, "
                                           "mediumImage, "
                                           "datasheet_url, "
                                           "modelNumber, "
                                           "productUrl, "
                                           "customerRating, "
                                           "numReviews, "
                                           "store, "
                                           "created_at)"
                                f" VALUES ('{web_no}',"
                                        f" '{title}', "
                                        f"'{crumbs}', "
                                        f"'{short}', "
                                        f"'{desc}', "
                                        f"'{hay}', "
                                        f"'{brand}', "
                                        f"'{image}', "
                                        f"'{pdf_link}', "
                                        f"'{model_no}', "
                                        f"'{url}', "
                                        f"{rating}, "
                                        f"{num_reviews}, "
                                        f"'{store}', "
                                        f"'{datetime.now()}')")
            cursor.execute(sql)
    
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()
    except:
        print('fail')
        nogo.append(url)
        continue
    finally:
        connection.close()






connection = pymysql.connect(host='tesla.epa.gov',
                             user='rdebbout',
                             password='Donsende1',
                             db='prod_racp',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = ("INSERT INTO products (itemId, "
                                       "name, "
                                       "categoryPath, "
                                       "shortDescription, "
                                       "longDescription, "
                                       "brandName, "
                                       "mediumImage, "
                                       "datasheet_url, "
                                       "modelNumber, "
                                       "productUrl, "
                                       "customerRating, "
                                       "numReviews, "
                                       "created_at)"
                            f" VALUES ('{web_no}',"
                                    f" '{title}', "
                                    f"'{crumbs}', "
                                    f"'{desc}', "
                                    f"'{hay}', "
                                    f"'{brand}', "
                                    f"'{image}', "
                                    f"'{pdf_link}', "
                                    f"'{model_no}', "
                                    f"'{url}', "
                                    f"{rating}, "
                                    f"{num_reviews}, "
                                    f"'{datetime.now()}')")
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = f"SELECT * FROM products WHERE itemId='{web_no}'"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
    
connection.close()
count = 0
for url in urls:
    if url[:12] == '/collection/':
        urls.pop(urls.index(url))
        count += 1
    
stupid = urls.copy()
