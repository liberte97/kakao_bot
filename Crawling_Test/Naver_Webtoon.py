from bs4 import BeautifulSoup
from pprint import pprint
import requests

'''
[+] Data request
    - Webpage source collect
'''

html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

"""
'''
[+] Data Parsing : 요일별
    - Webtoon extract
    - weekly webtoon
    - data 1 = webtoon section -> if find : 요일별, findAll : 전체요일
    - data 2 = title name section
'''

data1 = soup.findAll('div', {'class' : 'col_inner'})
pprint(data1)

data2 = data1.findAll('a', {'class' : 'title'})
pprint(data2)

''' 
[+] Text Extract
    - ref = https://wikidocs.net    
    - Data Parsing -> store list
    - Data Parsing -> text extact -> store list
'''

title_list = []
for t in data2:
    title_list.append(t.text)

pprint(title_list)

title_list = [t.text for t in data2]
pprint(title_list)

"""

"""
'''
[+] Data Parsing : 전체 요일
    - 전체 요일 -> 해당 요일 -> 영역 제목 -> 추출
    - extend : 요일상관 없이 전체로
    - append : 요일별로 나눠서
'''

data1_list = soup.findAll('div', {'class' : 'col_inner'})
week_title_list = []
for data1 in data1_list:
    data2 = data1.findAll('a', {'class' : 'title'})
    title_list = [t.text for t in data2]
    # pprint(title_list)
    week_title_list.extend(title_list)    
    # week_title_list.append(title_list)

pprint(week_title_list)
"""

'''
[+] Data Parsing : 전체요일2
    - only all data title
'''

data1 = soup.findAll('a', {'class' : 'title'})
week_title_list = [t.text for t in data1]
print(week_title_list)