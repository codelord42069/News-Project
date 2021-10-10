import requests
import pandas as pd

r = requests.get('https://www.dailymail.co.uk/home/index.html')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

results = soup.find_all('a' , attrs={'itemprop':'url'})
#finds everything in span tag where class=short-desc

print(len(results))
print(results)

records=[]
for result in results:
    lie = result
    records.append(lie)


 


df = pd.DataFrame(records, columns=[""])

#df['date'] = pd.to_datetime(df['date'])

df.to_csv('dailymail_headlines.csv', index=False, encoding='utf-8')




