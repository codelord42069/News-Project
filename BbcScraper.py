import requests
import pandas as pd

r = requests.get('https://www.bbc.co.uk/news')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

hrefs=[]
headlines = []
    
for link in soup.find_all('a' , href=True, attrs={'class':'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'}):

    link['href'] = 'https://www.bbc.co.uk' + link['href'] 
    hrefs.append(link['href'])

    heading = link.find('h3' , attrs={'class':'gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text'})

    headingText = heading.text
    headlines.append(headingText)
  
d = {'headlines': headlines, 'URL': hrefs}
df = pd.DataFrame(data=d)

df.to_csv('bbc_headliness.csv', index=False, encoding='utf-8')

print('BBC Done')

