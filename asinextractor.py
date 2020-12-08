#the main aim of this program is to retrive all ASIN's of product


import bs4,requests,re
print('enter the url of product')
prod_url = input()
res=requests.get(prod_url)
#print(res.text)
try:
    res.raise_for_status()
    regexobj=re.compile(r'.*?data-asin=("\w\w\w\w\w\w\w\w\w\w").*?')
    asinlists=regexobj.findall(res.text)
    playfile=open('asin.txt','w')
    for asin_code in asinlists:
        playfile.write(asin_code)
    playfile.close()
except:
    #error 503:server is too busy so try agian later
    print('Error:503 Your request can\'t be processed ')
