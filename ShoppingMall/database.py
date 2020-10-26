import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import ssl
import datetime
import pymysql
#context = ssl._create_unverified_context()

url = "https://smartstore.naver.com/mojjimoddi/category/ALL?cp=1"


conn = pymysql.connect(host='localhost', user='root', password='wlthgml97', db='crawling',charset = 'utf8')

curs = conn.cursor()
sql = "select * from mojjimoddi"
curs.execute(sql)

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
items = soup.find_all("li",attrs={"class":"-qHwcFXhj0"})

def store(title,price , review,link):
    curs.execute(
        "INSERT INTO mojjimoddi (title,price,review,link) VALUES (\"%s\", \"%s\", \"%s\",\"%s\")", (title, price,review,link)
    )
    curs.connection.commit()

for item in items:
    title = item.find("strong").get_text()
    price = item.find("span",attrs={"class":"nIAdxeTzhx"}).get_text()
    link = "https://smatstore.naver.com" + item.a["href"]
    review = item.find("div",attrs={"class":"_27Y22p2kob"})
    #review = item.find("em",attrs={"class":"_1dH1kEDaAZ"})
    if review:
        review = review.get_text()
    else:
        review = "no rivew, no star"

    store(title,price , review,link)
#result = curs.fetchall

curs.close()
conn.close()