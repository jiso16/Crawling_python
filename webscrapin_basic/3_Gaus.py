import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# 특정 만화 시리즈의 제목과 링크 불러오기 한개만
cartoons = soup.find_all("td", attrs = {"class":"title"})

# 특정 만화 시리즈의 제목과 링크 불러오기 (시리즈 전체)
for cartoon in cartoons:
    title = cartoon.a.get_text()
    link = "https://comic.naver.com" + cartoon.a["href"]
    print(title,link)

#평점 구하기
cartoons = soup.find_all("div",attrs = {"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)

