import requests
import pandas as pd

r = requests.get('https://www.bbc.co.uk/news')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('h3' , attrs={'class':'gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text'})


hrefs=[]

for a in soup.find_all('a' , href=True, attrs={'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'}):
    hrefs.append(a['href'])




#[i['href'] for i in soup.find_all('a', href=True)]

#hrefs = soup.find_all('h3' , attrs={'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor',})

#finds everything in span tag where class=short-desc


#print(hrefs) 

    



records=[]
for result in results:
    lie = result
    records.append(lie)

#print (records) 





d = {'col1': [records], 'col2': [hrefs]}

df = pd.DataFrame(data=d)


print(df) 

#df['date'] = pd.to_datetime(df['date'])

#df.to_csv('bbc_headlines.csv', index=False, encoding='utf-8')




