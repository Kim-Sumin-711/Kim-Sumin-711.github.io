import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import re

#강의에서는 kbs뉴스 box의 페이지를 하나씩 로드해가며 스크랩을 진행함
#여기서는 bbc의 뉴스 중 US&Canada, UK, Asis등 나라별 뉴스의 기사들을 스크랩해볼 것이다.
#강의에서 다뤘던 내용은 페이지네이션
#쉽게 말해 페이지를 돌면서 크롤링하는 기술임.
#구글을 예시로 들면 검색결과 밑에 1,2,3,4... 페이지가 뜨는데
#그것을 webdriver로 자동이동하고, 그곳에 있는 정보를 긁어오는 것이다.
#구글 뉴스페이지를 예시로 들면, 구글에 검색어를 입력하고 뉴스탭으로 넘어가면 여러 기사가 뜨는데,
#검색결과 1페이지나 n페이지나 html상으로 정보를 구성해놓은 구조가 똑같기 때문에
#url을 동적으로 수정하든가 webdriver에서 버튼을 자동으로 누르도록 하든가 해서
#여러페이지에 같은 크롤링 코드를 반복하여 적용시키는 것이 페이지네이션의 응용 사례 중 하나임. (매우 기본)
#페이지네이션을 이용하여 같은 코드를 여러번 작성하지 않아도 됨. (그냥 반복문에 넣어버려!!!)

#일단 기본세팅. 04-1 코드 그대로 가져옴
def get_html(url):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    #드라이버 열고
    driver.get(url)
    #로딩 최대 10초까지는 기다려주고,
    wait = WebDriverWait(driver,10)
    #html소스를 가져온다.
    html = driver.page_source
    #그리고 driver는 퇴근
    driver.quit()
    #html.parser보다 더 빠른 lxml을 사용
    soup = BeautifulSoup(html,'lxml')
    #soup를 리턴하자
    return soup


#각 나라별로 URL에 추가되는 부분이다. 따로 리스트에 담아서 for문을 돌려보자.
what_will_be_added_to_the_URL = ["us-canada","uk","world/africa","world/asia","world/australia",
                                 "world/europe","world/latin_america","world/middle_east"]

#뉴스 링크, 제목, 오버뷰만 가져올 것이니 미리 리스트를 정의하자.
news_links =[]
news_titles = []
news_overviews = []

#for반복문을 돌며 url을 적절히 수정한다.
for added_to_url in what_will_be_added_to_the_URL:
    url = "https://www.bbc.com/news/" + added_to_url
    total_soup = get_html(url)
    #total_soup에서 특정 div만 가져올 것이다.
    #직접 페이지에 들어가보면 뉴스 기사들 블록 여러개가 페이지를 구성하고 있다.
    #그 블록들은 class명이 다른 페이지에서도 통일되어 있기에 그 class명을 이용하여 div를 하나만 가져온다.
    #가장 상단에 있는 최신뉴스들만 볼거니까 find로 가장 먼저 발견되는거 하나만 가져온다.
    target_news_block = total_soup.find("div",class_ = "sc-ba42a659-2 jqWjKw")
    #bbc뉴스페이지를 훑어보면 뉴스 피드 카드 종류가 여러 개로 나뉘는 것을 볼 수 있었다.
    #london카드랑 edinburgh카드, manchester카드 등이 있다.
    #최신 뉴스 블록에는 여러 종류 카드가 섞여 있다. 그래서 card로 끝나는 data-testid를 가진 obj만 선별해서
    #cards리스트에 저장한다.
    cards = []
    for each_div in target_news_block.find_all("div"):
        #re 라이브러리를 쓸건데 이거는 밑에서 설명함.
        testid = each_div.get("data-testid")
        if not testid == None:
            if re.search(r"card$",testid):
                cards.append(each_div)
    #re라이브러리는 문자열을 검색,매칭,변환할 수 있도록 지원하는 아이임.
    #여기서는 문자열에서 첫번째로 일치하는 부분을 검색하는 search메소드와
    #r string 을 사용함.
    #r"card$"는 card로 끝나는지 확인하는데 쓰임. $는 문자열의 끝을 의미.
    #그래서 저 패턴이 처음으로 나타나는 곳을 문자열에서 검색함.

    #이제 채워진 cards 리스트에서 최신 뉴스들의 link와 title, overview를 가져와보자.
    #href, h2와 p만 뽑아내서 저장하면 끝이다.
    #미리 위에서 저장한 세개의 리스트에 저장할 것이다.
    for each_card in cards:
        link = "https://www.bbc.com"+each_card.find("a").get("href")
        title = each_card.find("h2").text
        overview = each_card.find("p").text
        news_links.append(link)
        news_titles.append(title)
        news_overviews.append(overview)
    #이 작업까지 완료했으면 다음 url에서 똑같이 작업하자. 페이지네이션

#페이지네이션을 통해 가져온 데이터를 csv로 만들자.
news_info_dict = {"News_Link":news_links,
                  "News_Title":news_titles,
                  "News_Overview":news_overviews}
news_info_df = pd.DataFrame(news_info_dict)
news_info_df.to_csv("csv/04_2_bbc_world_news.csv",index=False)


#추신
#필자는 저 코드를 실행시키면서 [12224:27852:0130/230516.360:ERROR:command_buffer_proxy_impl.cc(331)] GPU state invalid after WaitForGetOffsetInRange.
#이딴 오류메시지가 떴는데 앞에 숫자들은 프로세스ID,스레드ID,타임스템프이고,
#글자를 읽어보면 wait어쩌고 후에 GPU상태가 유효하지 않다고 한다.
#GPU의 command buffer에서 비정상적인 상태가 감지되었다는 메시지이다.
#chatgpt왈, GPU 하드웨어 가속 관련 문제거나 브라우저나 앱에서의 하드웨어 가속 버그라고 한다.
#뭔지는 잘 모르겠는데 일단 스크랩이 잘 되었으니 이런게 있구나 정도로만 훑고 넘어감.

#추신+
#04_2 의csv를 보면 기사가 70개가 넘는다.
#웹페이지 겉으로 나타난 기사는 당시에 58개 였는데 몇개가 중복해서 스크랩되었다.
#그 이유를 살펴보니 div에서 ~card를 data-testid로 갖는 elem중에서
#겉으로 들어나지는 않지만 중복된 뉴스 정보를 담고 있는 elem이 한 페이지에 하나씩은 있었다.
#그래서 기사가 중복된 것 같다.

