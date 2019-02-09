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
response  = requests.get(url, headers=headers)
response.status_code
data = response.text
soup = BeautifulSoup(data)
mydivs = soup.findAll("div", {"class": "content"})

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

# =============================================================================
# above gets me all of the grouped urls from the sitemap w/o the header groups
# header being the bolded <li> this is why I find the parent and check it's not
# a <b> tag.
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
len(list(set(p)))
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
        
        
##############################################################################

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
