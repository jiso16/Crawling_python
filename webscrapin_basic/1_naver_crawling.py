import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
print(soup.title)

#처음 a가 발견되는 element 출력
#print(soup.a)

#print(soup.a["href"])

#class = "Nbtn_upload"인 a element를 찾아줘
#print(soup.find("a", attrs = {"class":"Nbtn_upload"}))

#class = "Nbtn_upload"인 어떤 element를 찾아줘
#print(soup.find(attrs = {"class":"Nbtn_upload"}))

#print(soup.find("li",atters = {"class":"rank01"}))

#rank1 = soup.find("li",attrs = {"class":"rank01"})
#print(rank1.a.get_text())

#next_sibling으로 다음 테그까지 불러올 수 있음
#print(rank1.next_sibling.next_sibling)

# next_sibling을 사용 안 해도 다음으로 "li"가 포함된 테그 찾음
#rank2 = rank1.find_next_sibling("li")
#print(rank2.a.get_text())

# find_next_siblings를 통해서 형제 테그 다 불러올 수 있음
#print(rank1.find_next_siblings("li"))

# text로 불러올 수 있음
webtoon = soup.find("a",text="외모지상주의-306화 김기명 [05]")
#외모지상주의-306화 김기명 [05]

print(webtoon)