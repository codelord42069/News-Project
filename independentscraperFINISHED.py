import requests
import pandas as pd

r = requests.get('https://www.independent.co.uk')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

hrefs=[]
records = []






for link in soup.find_all('a' , attrs={'class':'title'}):


    
    link['href'] = 'https://www.independent.co.uk' + link['href'] 
    hrefs.append(link['href'])

   

    heading = link

    headingText = heading.contents
    

    records.append(headingText[0])



d = {'Headline': records, 'URL': hrefs}
df = pd.DataFrame(data=d)


df.to_csv('independent_headlines.csv', index=False, encoding='utf-8')




