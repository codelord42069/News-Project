import requests
import pandas as pd

r = requests.get('https://metro.co.uk/')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('span' , attrs={'class':'colour-box'})
#finds everything in span tag where class=short-desc

print(len(results))
print(results)

records=[]
for result in results:
    lie = result.text
    records.append(lie)


 


df = pd.DataFrame(records, columns=[""])

#df['date'] = pd.to_datetime(df['date'])

df.to_csv('metro_headlines.csv', index=False, encoding='utf-8')




