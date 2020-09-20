from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

'''
[+] Data requests
    - Naver wheather data collect
'''
html = requests.get("http://search.naver.com/search.naver?query=날씨")
# pprint(html.text)

''' 
[+] Data parsing 
    - All html text parsing
'''
# print(dir(bs))
soup = bs(html.text, 'html.parser')

# find class -> 요소 1개
data1 = soup.find('div', {'class':'detail_box'})

# find class -> all
data2 = data1.findAll('dd')

''' 
[+] Original Bring Text
    - ref = https://wikidocs.net    
    - Data Parsing -> span
'''
find_dust = data2[0].find('span', {'class' : 'num'}).text
ultra_find_dust = data2[1].find('span', {'class' : 'num'}).text
find_ozone = data2[2].find('span', {'class' : 'num'}).text


''' 
[+] Change Bring Text   
    - Data Parsing -> data2 number's repeat
'''
NumericalData = []
for i in range(len(data2)):
    NumericalData.append(data2[i].find('span', {'class' : 'num'}).text)

print("[+] Today Wheather")
print(NumericalData)