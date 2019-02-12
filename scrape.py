# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:13:20 2018

This script will take urls that have been previously collected with the 
"gather.py" script and call them with both BeautifulSoup and selenium to get
the data from each URL and load it into the DB "prod_racp".

When running this script from the command line use the following syntax....
    > python scrape.py <username> <password>

If exceptions are thrown the URL in question will be stored in a ".npy" file
that will hold it as well as the error message which can be parsed later to 
troubleshoot any URLS that don't get picked up.

I have the following error coming up when running this from the cmd prompt:

    [29744:43676:0211/172506.507:ERROR:platform_sensor_reader_win.cc(242)] NOT IMPLEMENTED

which I think this page may address with the version of chrome used being 
the problem, but it still seems to be working fine with this message. 
    
    https://stackoverflow.com/questions/50424654/python-selenium-how-to-ignore-shader-cache-error

@author: Rdebbout
"""
import os
import re
import sys
import requests
import numpy as np
import pymysql.cursors
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime

def get_state(user, password):
    '''
    Find the state of the DB currently so we can remove any URLs that have 
    already been scraped from the array so as not to repeat in the event of a
    shutdown or unhandled exception. The "web_no" will be used to increment
    a value for the itemId column.
    '''
    connection = pymysql.connect(host='tesla.epa.gov',
                                 user=user,
                                 password=password,
                                 db='prod_racp',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.Cursor)
    
    try:
        with connection.cursor() as cursor:

            sql = f"SELECT productUrl FROM products WHERE store = 'Home Depot'"
            cursor.execute(sql)
            db = cursor.fetchall()
            sql = "SELECT MAX(itemID) from prod_racp.products"
            cursor.execute(sql)
            (web_no,) = cursor.fetchone()
    finally:
        connection.close()
    done = [url.split('www.homedepot.com')[-1] for (url,) in db]
    return web_no, done

def strip_clean(text):
    '''
    Reduce duplicate whitespaces to one and replace newlines
    '''
    return re.sub(r'\s+', ' ', text.replace('\n',''.strip()))

def gather_data(url, soup):
   
    model_no = soup.find("h2", {"class": "product_details modelNo"})
    model_no = model_no.text.split('#')[-1].strip() if model_no else ''
    brand = soup.find("h2", {"class": "product-title__brand"})
    brand = brand.text.strip() if brand else ''
    title = soup.find("h1", {"class": "product-title__title"}).text.strip()
    image = soup.find("img", {"id": "mainImage"})['src']
    short = soup.find("meta", {"name": "description"})['content']
    short = short.replace("'","") if short else ''
    desc = soup.find("p", {"itemprop": "description"}).text.replace('\n','').strip().replace('\'','')
    li = soup.find("div", {"class": "main_description"}).findAll("li")
    if li:
        desc = desc + '\n**' + '\n**'.join([strip_clean(x.text) for x in li])
    p = soup.find('div',{'id':'specsContainer'})
    hold={}
    heads = p.findAll('div',{'class':'specs__title'})
    tabs = p.findAll('div',{'class':'specs__table'})
    for head, tab in zip(heads,tabs):
        second = {}
        for grp in tab.findAll('div',{'class':'specs__group'}):
            lbl = grp.findNext('div',{'class':'specs__cell--label'})
            cell = lbl.findNext('div',{'class':'specs__cell'})
            second[lbl.text] = cell.text
        hold[strip_clean(head.text)] = second
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
    crumbs = '/'.join([crumb.text for crumb in bread])
    hay = ''
    for k,v in hold.items():
        hay += k + '\n'
        for i,j in v.items():
            hay += '  -' + i + ': ' + j +'\n' 
    hay = hay.replace('\'','') # remove ' chars cause it will fail on entering into DB
    desc = desc.replace('\'','')
    brand = brand.replace('\'','')
    title = title.replace('\'','')

    return {'title': title,'crumbs':crumbs, 'short':short, 'desc':desc,
            'hay':hay, 'brand':brand, 'image':image, 'pdf_link':pdf_link,
            'model_no':model_no, 'rating':rating, 'num_reviews':num_reviews}
 
                      
if __name__ == '__main__':
  
    headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/69.0.3497.100 Safari/537.36')}

    user = sys.argv[1]
    password = sys.argv[2]
    
    (web_no, db_urls) = get_state(user,password)

    total = np.load('unique_urls.npy').tolist()
    urls = list(set(total)-set(db_urls)) # filter out those already in DB!
    urls = [f"https://www.homedepot.com{url}" for url in urls]
    

    if os.path.exists('nogo.npy'):
        nogo = np.load('nogo.npy').tolist()
        messed = [n.split(': insert :')[0] for n in nogo]
        urls = list(set(urls)-set(messed))
    else:
        nogo = []
        
    print (f"there are {len(urls)} urls that need to be searched")
    
    browser = webdriver.Chrome()
    store = "Home Depot"
    
    # for testing....
#    urls = urls[:17]
    
    for i, url in enumerate(urls):
        web_no += 1
        print(f"gathering itemId: {web_no}...")
        response  = requests.get(url, headers=headers)
        data = response.text
        soup = BeautifulSoup(data, features="html.parser")

        connection = pymysql.connect(host='tesla.epa.gov',
                                 user=user,
                                 password=password,
                                 db='prod_racp',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    
        try:
            
            d = gather_data(url, soup) 

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
                                            f" '{d['title']}', "
                                            f"'{d['crumbs']}', "
                                            f"'{d['short']}', "
                                            f"'{d['desc']}', "
                                            f"'{d['hay']}', "
                                            f"'{d['brand']}', "
                                            f"'{d['image']}', "
                                            f"'{d['pdf_link']}', "
                                            f"'{d['model_no']}', "
                                            f"'{url}', "
                                            f"{d['rating']}, "
                                            f"{d['num_reviews']}, "
                                            f"'{store}', "
                                            f"'{datetime.now()}')")
                cursor.execute(sql)  
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
        except Exception as e:
            nogo.append(f"{url}: insert : {e}")
            np.save('nogo.npy',nogo)
            continue
        finally:
            connection.close()
    browser.quit()
####################################################        