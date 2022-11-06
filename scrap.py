import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np







final=pd.DataFrame()

for j in range(1,111):
    
    url='https://www.ambitionbox.com/list-of-companies?page={}'.format(j)
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)AppleWebkit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
    webpage=requests.get(url, headers=headers).text
    
    soup=BeautifulSoup(webpage, 'lxml')
    
    company=soup.find_all('div', class_='company-content-wrapper')
    
    name=[]
    rating=[]
    reviews=[]
    ctype=[]
    hq=[]
    old=[]
    employees=[]


    for i in company:

        name.append(i.find('h2').text.strip())
        rating.append(i.find('p',class_='rating').text.strip())
        reviews.append(i.find('a',class_='review-count').text.strip())
        ctype.append(i.find_all('p', class_='infoEntity')[0].text.strip())
        hq.append(i.find_all('p', class_='infoEntity')[1].text.strip())
        old.append(i.find_all('p', class_='infoEntity')[2].text.strip())
        try:
            employees.append(i.find_all('p', class_='infoEntity')[3].text.strip())
        except:
            employees.append(np.nan)


    d={'name':name, 'rating':rating, 'reviews':reviews, 'type':ctype,'hq':hq, 'old':old, 'employees':employees}

    df=pd.DataFrame(d)

    final=final.append(df)
    print(final)
