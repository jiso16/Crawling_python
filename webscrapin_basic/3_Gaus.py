import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


# 특정 만화 시리즈의 제목과 링크 불러오기 한개만
#cartoons = soup.find_all("td", attrs = {"class":"title"})
# title = cartoons[1].a.get_text()
# link = cartoons[1].a["href"]
# print(title)
# print("https://comic.naver.com"+link)


# # 특정 만화 시리즈의 제목과 링크 불러오기 (시리즈 전체)
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title,link)

#평점 구하기

cartoons = soup.find_all("div",attrs = {"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)

