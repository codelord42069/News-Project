import requests
import pandas as pd

r = requests.get('https://www.theguardian.com/uk')

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

hrefs=[]
records = []






for link in soup.find_all('a' , href=True, attrs={'class':'u-faux-block-link__overlay js-headline-text'}):


    
    hrefs.append(link['href'])

   

    heading = link.find('a', attrs={'class':'u-faux-block-link__overlay js-headline-text'})
    if heading:
        headingText = heading.string
    else:
        headingText = ''
    records.append(heading)
  
d = {'Headline': records, 'URL': hrefs}
df = pd.DataFrame(data=d)


df.to_csv('guardian_headlines.csv', index=False, encoding='utf-8')


print('Done')








# results = soup.find_all('a', attrs={'class':'u-faux-block-link__overlay js-headline-text'})
# #finds everything in span tag where class=short-desc

# print(len(results))

# records=[]
# for result in results:
#     lie = result.contents
#     records.append(lie)


 


# df = pd.DataFrame(records, columns=[""])

# #df['date'] = pd.to_datetime(df['date'])

# df.to_csv('guardian_headlines.csv', index=False, encoding='utf-8')





