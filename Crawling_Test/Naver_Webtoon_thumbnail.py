from bs4 import BeautifulSoup
from pprint import pprint
import requests


'''
[+] Storage 
    - Folder Create
'''

try:
    if not (os.path.isdir('image')):
        os.makedirs(os.path.join('image'))
except OSError as e:
    if e.errno != error.EEXIST:
        print("Fail")
        exit()

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
'''
"""

data1List = soup.findAll('div', {'class':'col_inner'})

liList = []
# Webtoon List
for data1 in data1List:
    # Title, Thumbnail extract
    liList.extend(data1.findAll('li'))

# Thumbnail + Title
for li in liList:
    img = li.find('img')
    title = img['title']
    img_src = img['src']
    title = re.sub('[^0-9a-zA-zr-힗]', '', title)

    urlretrieve(img_src, './imgage/'+title+'.jpg')

