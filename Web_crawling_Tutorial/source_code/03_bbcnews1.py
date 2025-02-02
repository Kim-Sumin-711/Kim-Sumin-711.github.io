import requests
from bs4 import BeautifulSoup
import pandas as pd

url1 = 'https://www.bbc.com/news/articles/c93l8w5ldkpo'
html_doc1 = requests.get(url1).text
#print(html_doc)

soup1 = BeautifulSoup(html_doc1,"html.parser")
#print(soup)

#find 가장 먼저 있는거 하나만
#find_all 다 가져와
title1= soup1.find('h1',class_="sc-518485e5-0 bWszMR")
#print(title1.text)

body1 = soup1.find('p',class_="sc-eb7bd5f6-0 fYAfXe")
print(body1.text)

data = {'뉴스url' : [url1], '제목' : [title1.text], '내용':[body1.text]}
#data를 DataFrame구조로 만들어버리기.
df = pd.DataFrame(data)

#df를 csv로 저장하기
df.to_csv('csv/02_news1_bbc.csv')
#index=True가 기본값
#True이면 a열에 인덱스가 있음. 0부터 시작함.
#False로 지정하려면 parameter에 index=False로 주자.

url_list = [url1]
title_list = [title1.text]
body_list = [body1.text]

url2 = 'https://www.bbc.com/future/article/20250114-five-science-backed-daytime-hacks-to-improve-your-sleep'
html_doc2 = requests.get(url2).text
#.text안붙이고 get보내서 저장하고 출력하면 <response [200]>형식이 출력됨.

soup2 = BeautifulSoup(html_doc2,'html.parser')
title2 = soup2.find('h1', class_ = "sc-518485e5-0 bWszMR")
body2 = soup2.find('p',class_='sc-eb7bd5f6-0 fYAfXe')

url_list.append(url2)
title_list.append(title2.text)
body_list.append(body2.text)

data["뉴스url"] = url_list
data['내용'] = body_list
data['제목'] = title_list

df2 = pd.DataFrame(data)
df2.to_csv("csv/02_news12_bbc.csv",index=False)

#url을 가져온 이후부터 파싱, 추출하는 과정은 동일하기 때문에
#url_list에서 하나씩 elem가져와서(for문 등으로) 작업을 해도 된다.
#아니면 모듈화 하든가  