import urllib.request as req
from bs4 import BeautifulSoup

# HTTP Get requests
res = req.urlopen("https://www.sappun.co.kr/")

soup = BeautifulSoup(res, 'html.parser')
#유니코드 에러 해결을 위한 utf8 -> CP949로 변경

print(soup.find_all(class_="MS_prod_img_s"))
#print(soup.find_all(class_="item_title"))
