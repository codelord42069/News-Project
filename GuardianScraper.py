import requests
import pandas as pd

r = requests.get('https://www.theguardian.com/uk')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

hrefs=[]
headlines=[]

for link in soup.find_all('a' , href=True, attrs={'class':'u-faux-block-link__overlay js-headline-text'}):

    hrefs.append(link['href'])
    headlines.append(link.contents[0])
    
d = {'Headline': headlines, 'URL': hrefs}
df = pd.DataFrame(data=d)

df.to_csv('guardian_headlines.csv', index=False, encoding='utf-8')
print('Guardian Done')



