import requests
import pandas as pd

r = requests.get('https://www.theguardian.com/uk')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('a', attrs={'class':'u-faux-block-link__overlay js-headline-text'})
#finds everything in span tag where class=short-desc

print(len(results))
print(results)

records=[]
for result in results:
    lie = result.contents
    #date = result.find('strong').text[0:-1] + ', 2017'
    records.append(lie)


 


df = pd.DataFrame(records, columns=[""])

#df['date'] = pd.to_datetime(df['date'])

df.to_csv('guardian_headlines.csv', index=False, encoding='utf-8')




