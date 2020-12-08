#The main aim of this code is to read asins from asin file and scrape the product data like product rating,product price, and other technical details

import re,requests,bs4,time

def amazon_prod_name(html_text):  #This function retutrns product title for the given html text
    
    regexobj=re.compile(r'<span id="productTitle" class="a-size-large">\s*(\w.*?)\n\s*</span>',re.DOTALL)             #regular expression for product-title
    pt=regexobj.findall(html_text)
    prod_name=pt[0]
    return prod_name


def amazon_product_details(html_text):  #This function returns product details which contain product features

    regexobj=re.compile(r'<tr>\s*<td class="label">(.*?)</td>\s*<td class="value">(.*?)</td>\s*</tr>',re.DOTALL)
    pd=regexobj.findall(html_text)
    return pd


def customer_review(html_text):  #This function returns average customer rating of the product
    
    regexobj=re.compile(r'<span id="acrPopover" class="reviewCountTextLinkedHistogram noUnderline" title="(\d.\d) out of 5 stars">',re.DOTALL)
    cr=regexobj.findall(html_text)
    return cr


def product_price(html_text):    #This function returns price of product on amazon

    regexobj=re.compile(r'<span id="priceblock_(ourprice|saleprice)" class="a-size-medium a-color-price"><span class="currencyINR">&nbsp;&nbsp;</span> (.*?)</span>',re.DOTALL)
    price=regexobj.findall(html_text)
    return price


#let's read the asin file and write in asin-lists

playfile=open('asin.txt','r')
asinlists=(playfile.readline()).split('\""')
playfile.close()
asinlist=asinlists[0]
asinlists[0]=asinlist[1:]
asinlist=asinlists[len(asinlists)-1]
asinlists[len(asinlists)-1]=asinlist[:10]

for i in asinlists:
    print(i)

stnd_url='http://www.amazon.in/dp/'

urllists=[]
for i in asinlists:
    new_url=stnd_url+i    #when you want to search for a product in amazon you to just add product's asin code to standard url it will redirect to that product page
    urllists.append(new_url)

html_lists=[]

for i in urllists:
    res=requests.get(i)
    while res.status_code!=200:
        res=requests.get(i)
    html_lists.append(res.text)

print(html_lists[0])
for i in html_lists:
    prod_name=amazon_prod_name(i)
    print(prod_name)

for i in html_lists:
    prod_details=amazon_product_details(i)
    print(prod_details)

for i in html_lists:
    rating=customer_review(i)
    print(rating)

for i in html_lists:
    price=product_price(i)
    print(price)
