'''
맨날 잡플래닛 평점 검색해서 보는 거 귀찮아서 만듬
'''

import requests
from bs4 import BeautifulSoup

keyword = input('검색할 회사명을 입력해 주세요\n')

url = 'https://www.jobplanet.co.kr/search?category=&query=' + keyword + '&_rs_act=index_new&_rs_element=main_search_bar'

req = requests.get(url)

# print(req.text)

soup = BeautifulSoup(req.text, 'html.parser')
