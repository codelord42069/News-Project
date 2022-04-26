import requests
import pandas as pd

import timeit
start = timeit.default_timer()

r = requests.get('https://www.dailymail.co.uk/home/index.html')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser') 



hrefs=[]
headlines=[]

for link in soup.find_all('a' , attrs={'itemprop':'url'}):

    link['href'] = 'https://www.dailymail.co.uk' + link['href'] 
    hrefs.append(link['href'])

    headlines.append(link.contents[0])


d = {'Headline': headlines, 'URL': hrefs}
df = pd.DataFrame(data=d)

df.to_csv('dailymail_headlines.csv', index=False, encoding='utf-8')
print("Daily Mail Done")

stop = timeit.default_timer()
print('Time: ', stop - start)  




