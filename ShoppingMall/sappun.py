import requests
from bs4 import BeautifulSoup

url = "https://www.sappun.co.kr"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# 제품명과 가격 불러오기 (weekly best 전체)
best_titles = soup.find_all("div",attrs = {"class":"item-price-wrap"})
# section_title = soup.find("h3",text="WEEKLY BEST")
# print(section_title)

for best_title in best_titles:

    title = best_title.find("div").get_text()
    price = best_title.find("span").get_text()
    if best_title.find("strike").get_text():
        best_title.parent
        for best_title in best_titles:
            price =best_title.find_next_siblings("span")
    print("title=", title, "price=", price)



# for cartoon in cartoons:
#     title = best_title[0].a.get_text()
#     #link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title)

