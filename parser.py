import urllib.request as req
import re

# HTTP Get requests
rep = req.urlopen("https://www.sappun.co.kr/")

#유니코드 에러 해결을 위한 utf8 -> CP949로 변경
data = rep.read().decode('CP949') 

result = re.findall('[./-_\w]+.jpg', data)
#f = pd.read_csv('directory/file', sep='|'', encoding='CP949')


print(result)