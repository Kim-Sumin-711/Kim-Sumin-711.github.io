import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

url = "https://www.bbc.com/"
html_doc = requests.get(url).text
#html.parser대신 lxml을 사용해봤다. lxml이 C로 작성되서 더 빠르다고 하는데 자세한건 나중에 알아보자.
soup = BeautifulSoup(html_doc,'lxml')

#지금부터 할 것은 하이퍼링크가 걸려있는 텍스트를 담은 뉴스 박스들을
#가져오는 활동을 할 것이다.
#하이퍼링크는 보통 html문서의 <a>태그에 담겨있다. <a href = 어쩌고></a>

box_contents = soup.find_all('a',class_ = "sc-2e6baa30-0 gILusN")


#만일 저기서 데이터가 안담겼다면
#1. 태그 이름 잘 담음?
#2. 페이지 소스에 JS가 사용됨?
#동적으로 데이터를 로딩하는데 JS가 쓰여서 Bs로 가져올 수 없는 경우도 있음.
#24-2H 예측하는 미래-통계와 확률 수업에서 크롤링 프로젝트를 진행할 때 보았던
#대학백과 등의 사이트가 그러했다.

#solution?
#셀레늄 Selenium
#웹 페이지를 자동으로 제어, 테스트 할 수 있는 도구. 직접적으로 웹 브라우저를 제어
#requests, beautifulsoup으로 크롤링 불가능 할 때, 원하는 결과를 가져오지 못할 때 : selenium

#정적 페이지 = requests + beautifulsoup
#서버로부터 한 번 요청하면 변하지 않는 형태의 HTMl로 작성된 페이지
#웹 서버는 클라이언트 요청이 들어올 때마다 미리 만들어 놓은 HTMl파일을 그대로 반환
#서버 측에서 미리 준비가 되어 있기 때문에, 클라이언트 측에서 별다른 처리 없이 바로 브라우저에 표시

#동적 페이지 = Selenium
#웹 서버로부터 HTMl파일을 받아온 다음, 브라우저가 해석하고 실행하면서, JS같은 스크립트 언어를 사용,동적으로 페이지를 만듦
#이렇게 생성된 HTMl > 데이터를 불러오거나, 우리가 입력하거나 스크롤 할 때 > 화면이 변경되는 등의 상호작용이 필요함.

#pip install selenium
#pip install webdriver_manager

#selenium으로 웹 드라이버를 실행
service = Service(executable_path=ChromeDriverManager().install())
#executable_path 에는 실행할 크롬 브라우저가 어디있는지 경로를 넣어주는 파라미터이다.
#여기서는 ChromeDriverManager가 설치된 경로를 넣어줌.

driver = webdriver.Chrome(service=service)
#위에서 작성한 service변수를 service파라미터에 넣어줌.

driver.get(url)

#기다려 : 10초 동안
#이거는 최대 10초동안 대기해달라는 의미
#그 전에 로딩이 완료되면 뒤의 작업을 진행함.
#동적으로 time.sleep을 제어하는 느낌이랄까?
wait = WebDriverWait(driver, 10)

#드라이버 접근 -> 웹 페이지의 소스를 가져온다.
html = driver.page_source

#드라이버를 종료함.
driver.quit()

#이제 가져온 소스와 BS를 사용해서 뉴스 박스를 가져오자
#리스트로
box_contents = soup.find_all('a',class_ = "sc-2e6baa30-0 gILusN")
#print(box_contents)

#print(len(box_contents))   ? 108개나 되네


#print(box_contents[10])
#강의에서는 news링크,이름,본문,생성일자 등을 받아왔지만
#여기서는 뉴스사진 설명, 뉴스 제목, 뉴스 소제목?, 뉴스 관련 지역을 받아온다.
#1차 시도로 data-testid라는 속성이 external_anchor인것만 받아오도록 해보았음.
#그런데 문제는 메뉴 목록에 있는 a태그들도 다 class이름이 똑같아서
#bbc광고나 bbc앱 설치 이런 데이터들도 같이 들어와서 별로 효과가 없었다.
#1차 시도 코드는 여기에 주석처리 시켜놓겠다.

'''external_anchor_contents = []
for cont in box_contents:
    testid = cont.get("data-testid")
    if(testid == "external-anchor"):
        external_anchor_contents.append(cont)

href_url_list=[]
thumbnail_explaination_list = []
news_title_list = []
news_overview_list = []
news_upload_time_list = []


#이제 external_anchor_contents에서 정보를 뽑아오자.
for news in external_anchor_contents:
    href_url = news['href']
    thumbnail_explaination = news.find('img',class_ = "sc-a34861b-0 efFcac")
    news_title = news.find("h2")
    news_overview = news.find("p")
    news_upload_time = news.find("span",class_="sc-6fba5bd4-2 bHkTZK")

    href_url_list.append(href_url)

    if(thumbnail_explaination != None):
        thumbnail_explaination_list.append(thumbnail_explaination.get('alt'))
    else:
        thumbnail_explaination_list.append("None")
    if(news_title != None):
        news_title_list.append(news_title.text)
    else:
        news_title_list.append("None")
    if(news_overview != None):
        news_overview_list.append(news_overview.text)
    else:
        news_overview_list.append("None")
    if(news_upload_time != None):
        news_upload_time_list.append(news_upload_time.text)
    else:
        news_upload_time_list.append("None")

bbc_box_news_contents_dict = {"link" : href_url_list,
                              "title" : news_title_list,
                              "overview" : news_overview_list,
                              "thumbnail_explaination" : thumbnail_explaination_list,
                              "upload_time" : news_upload_time_list}

df = pd.DataFrame(bbc_box_news_contents_dict)
df.to_csv("csv/04_bbcnews_box.csv",index=False)'''

#2차 시도로 무언가를 해보았다.
#04-1_bbc_tech_news_box.py를 참고하라.



