import requests
from bs4 import BeautifulSoup

url = "https://smartstore.naver.com/mojjimoddi/category/ALL?cp=1"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


items = soup.find_all("li",attrs={"class":"-qHwcFXhj0"})

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
    print(title,"/","price =", price,"won","/",review)
    print("link=",link)


