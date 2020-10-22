import pymysql
conn = pymysql.connect(host='localhost', user='root', password='wlthgml97', db='crawling',charset = 'utf8')

print("mojjimoddi")

cur = conn.cursor()
cur.execute('USE mojjimoddi')

print(cur.fetchone())
cur.close()
conn.close()