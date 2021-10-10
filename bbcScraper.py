import requests
import pandas as pd

r = requests.get('https://www.bbc.co.uk/news')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('h3' , attrs={'class':'gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text'})
#finds everything in span tag where class=short-desc

print(len(results))
print(results)

records=[]
for result in results:
    lie = result.text
    records.append(lie)


 


df = pd.DataFrame(records, columns=[""])

#df['date'] = pd.to_datetime(df['date'])

df.to_csv('bbc_headlines.csv', index=False, encoding='utf-8')




