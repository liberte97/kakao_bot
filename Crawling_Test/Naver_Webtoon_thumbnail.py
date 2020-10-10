from bs4 import BeautifulSoup
from pprint import pprint
import requests, os, re
from urllib.request import urlretrieve

'''
[+] Data request
    - Webpage source collect
'''

html = requests.get("http://comic.naver.com/webtoon/weekday.nhn")
soup = BeautifulSoup(html.text, 'html.parser')
html.close()

'''
[+] Data Parsing : 요일별
    - Webtoon extract
    - weekly webtoon
    - data 1 = webtoon section -> if find : 요일별, findAll : 전체요일
'''

try:
    if not (os.path.isdir('WebtoonThumbnail')):
        os.makedirs(os.path.join('WebtoonThumbnail'))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("폴더 생성 실패!")
        exit()

data1 = soup.findAll('div', {'class' : 'col_inner'})

li_list = []
for d in data1:
    li_list.extend(d.findAll('li'))

for li in li_list:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title)
    urlretrieve(img_src, './WebtoonThumbnail/', title+'.jpg')
