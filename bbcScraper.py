import requests
import pandas as pd

r = requests.get('https://www.bbc.co.uk/news')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')



hrefs=[]
records = []

for link in soup.find_all('a' , href=True, attrs={'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'}):

    if link['href'][0] == 'h':
        print(link['href'])
        hrefs.append(link['href'])

    else:
        link['href'] = 'https://www.bbc.co.uk' + link['href'] 
        hrefs.append(link['href'])

    heading = link.find('h3' , attrs={'class':'gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text'})
    if heading:
        headingText = heading.text
    else:
        headingText = ''
    records.append(headingText)
  


#nice





d = {'Headline': records, 'URL': hrefs}

df = pd.DataFrame(data=d)



#df['date'] = pd.to_datetime(df['date'])

df.to_csv('bbc_headlines.csv', index=False, encoding='utf-8')


print('Done')

