import requests
import pandas as pd


r = requests.get('https://www.dailymail.co.uk/home/index.html')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')


hrefs=[]
records = []


for link in soup.find_all('a' , attrs={'itemprop':'url'}):

    link['href'] = 'https://www.dailymail.co.uk' + link['href'] 
    hrefs.append(link['href'])

    heading = link
    headingText = heading.contents
    
    records.append(headingText[0])


d = {'Headline': records, 'URL': hrefs}
df = pd.DataFrame(data=d)


df.to_csv('dailymail_headlines.csv', index=False, encoding='utf-8')
print("Daily Mail Done")






