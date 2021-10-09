import requests
import pandas as pd

r2 = requests.get('https://www.thesun.co.uk/')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r2.text, 'html.parser')

results2 = soup.title.string('a', attrs={'data-headline':''})
#finds everything in span tag where class=short-desc

print(len(results2))
print(results2)

records2=[]
for result2 in results2:
    lie = result2.text
    #date = result.find('strong').text[0:-1] + ', 2017'
    records2.append(lie)


 


df2 = pd.DataFrame(records2,columns=[""])

#df['date'] = pd.to_datetime(df['date'])

df2.to_csv('thesun_headlines.csv', index=False, encoding='utf-8')