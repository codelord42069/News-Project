import requests
import pandas as pd

r = requests.get('https://www.independent.co.uk')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

hrefs=[]
headlines = []

for link in soup.find_all('a' , attrs={'class':'title'}):

    link['href'] = 'https://www.independent.co.uk' + link['href'] 
    hrefs.append(link['href'])

    headlines.append(link.contents[0])

d = {'Headline': headlines, 'URL': hrefs}
df = pd.DataFrame(data=d)

df.to_csv('independent_headlines.csv', index=False, encoding='utf-8')
print("Independent Done")






