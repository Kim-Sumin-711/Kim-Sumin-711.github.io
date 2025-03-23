import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

#2차 시도
#이번에는 tech뉴스쪽에 들어가서 필요한 div부분만 가져와서 시도해보자.
#latest headline쪽만 긁어보자.

#기본세팅
#url을 파라미터로 전송함. url을 driver로 열어서 html을 긁어온다. 후 bs로 파싱한 후 리턴함.
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

#우효옷 soup겟또다제~~
soup = get_html("https://www.bbc.com/innovation/technology")

#div를 추출해서 리스트 형태로 만든다음, 원하는 속성의 원하는 값이 있는 div만 가져온다.
def get_wanted_div_str(total_soup,wanted_attri,wanted_attri_val):
    '''total_soup는 bs로 파싱한 html,
    wanted_attri는 찾아보려는 attribute(속성)을 str로 입력
    wanted_attri_val은 해당 attribute(속성)에 있었으면 좋겠는 값을 str으로 입력.'''
    #해당 속성이 없거나 속성의 값이 스트링이 아닌 경우는 일단 넘어감.
    #div 태그를 가진 obj다 찾아주자.
    sections = total_soup.find_all("div")
    target_section = []
    #div가 담긴 리스트의 원소를 하나씩 빼서 wanted_attri가 wanted_attri_val을 할당받았는지 확인하고
    #원하는 거면 target_section에 저장.
    for each_section in sections:
        if(each_section.get(wanted_attri) == wanted_attri_val):
            target_section.append(each_section)
    #그리고 리턴한다.
    return target_section

#div에 있는 class속성의 text가 똑같을 가능성이 있으니 data-testid를 참고하자.
#참고로 data-* 이런 형식은 사용자가 임의로 정의한 속성이라고 chatgpt가 말한다. 나중에 자세히 알아보자.
#그리고 내가 원하는 latest headline이 담긴 div를 찾아야함.
#html을 개발자모드에서 살펴본결과, data-testid가 nevada-section-6인 것을 확인.
#다른 div는 data-testid가 다르다.
target_section = get_wanted_div_str(soup,"data-testid","nevada-section-6")

#확인해본 결과 data-testid 에 nevada-section-6이 유일하다는 것을 확인.

news_cards = []
#target section들에서 각 카드뉴스에 해당되는 구역(div)를 전부 찾아 news_cards에 리스트 형태로 저장.
#여기서는 어짜피 target_section이 하나라서 for문을 안써도 된다.
for each_target_section in target_section:
    tmp = each_target_section.find_all("div",class_ = "sc-c6f6255e-0 eGcloy")
    news_cards.extend(tmp)

#가져온 뉴스 카드 div에서 뉴스 링크, 뉴스 제목, 뉴스 overview, 업로드된 시간, 장르? 를 가져와보자.
#저장할 리스트
news_link = []
news_title = []
news_overview = []
news_uploaded_time = []
news_type = []
#뉴스 카드들의 원소를 하나씩 순회하자.
for each_card in news_cards:
    #해당되는 태그를 클래스명을 기준으로 찾아준다.
    #link같은 경우는 a태그의 href라는 속성에 담겨있으므로 get메소드를 사용했다.
    #href에 담긴 정보가 str이라서 .text를 사용하지 않아도 된다.
    link = "https://www.bbc.com" + each_card.find("a",class_ = "sc-2e6baa30-0 gILusN").get("href")
    #여기부터는 태그를 찾아준 후, 그 속의 text정보만을 가져온다.
    #즉 <h2></h2>이런거 때고 순수하게 text만 가져온다.
    title = each_card.find("h2",class_ = "sc-8ea7699c-3 dhclWg").text
    overview = each_card.find("p",class_ = "sc-b8778340-4 kYtujW").text
    uploaded_time = each_card.find("span",class_ = "sc-6fba5bd4-1 efYorw").text
    what_type = each_card.find("span", class_ = "sc-6fba5bd4-2 bHkTZK").text
    #리스트에 하나씩 저장한다.
    news_link.append(link)
    news_title.append(title)
    news_overview.append(overview)
    news_uploaded_time.append(uploaded_time)
    news_type.append(what_type)

#가져온 정보를 dictionary형태로 저장한다. 추후에 df로 변환시키기 위함.
bbc_card_news_dict = {"News_link":news_link,
                      "Title" : news_title,
                      "Overview" : news_overview,
                      "Uploaded_Time": news_uploaded_time,
                      "News_Type" : news_type}
#pandas.DataFrame으로 변환시킨다.
bbc_card_news_df = pd.DataFrame(bbc_card_news_dict)
#후에 to_csv메소드를 이용하여 csv파일로 저장한다.
bbc_card_news_df.to_csv("csv/04_1_bbc_tech_news_box.csv",index=False)


