#크롤링 할 사이트
#https://www.letskorail.com/ebizprd/prdMain.do

#크롤링 하기 전 robots.txt확인하기
#https://www.letskorail.com/robots.txt


from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
#이거는 Xpath로 어떤 요소를 찾아낼 때 씀
#여기서는 Xpath, '다음'버튼 클릭, 접속된 페이지의 url 가져오는 것 까지 수행할것이다.
from selenium.webdriver.common.by import By
import time
#time.sleep(2) 하면 2초 동안 절대적으로 대기함
#webDriverWait(driver,2)를 쓰면 웹 페이지가 로딩되기까지 최대 2초까지 기다림. 그 전에 로딩되면 넘어감
#둘이 다른 점은 sleep은 그냥 대기하는 거고, webDriverWait은 동적으로? 대기하는 것이다.

#Selenium 웹 드라이버 서비스 설정
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
#1차 시도시에는 "https://www.letskorail.com/ebizprd/EbizPrdTicketPr21111_i1.do"로 시도했다.
#그러나 조회하기를 누르면 저 링크 뒤의 & 어쩌고가 엄청 붙은 곳의 데이터를 한 페이지 보여주고,
#다음 페이지부터 직접 &어쩌고가 붙는 모양이다.
#링크 뒤의 &어쩌고의 규칙성을 찾기는 어려워서 그냥 두번째 페이지부터 긁어보았다.
url = "https://www.letskorail.com/ebizprd/EbizPrdTicketPr21111_i1.do?&txtGoAbrdDt=20250201&txtGoHour=065700&selGoYear=2025&selGoMonth=02&selGoDay=01&selGoHour=00&txtGoPage=2&txtGoStartCode=0001&txtGoStart=%EC%84%9C%EC%9A%B8&txtGoEndCode=0020&txtGoEnd=%EB%B6%80%EC%82%B0&selGoTrain=05&selGoRoom=&selGoRoom1=&txtGoTrnNo=&useSeatFlg=&useServiceFlg=&selGoSeat=&selGoService=&txtPnrNo=&hidRsvChgNo=&hidStlFlg=&radJobId=1&SeandYo=&hidRsvTpCd=03&selGoSeat1=015&selGoSeat2=&txtPsgCnt1=1&txtPsgCnt2=0&txtMenuId=11&txtPsgFlg_1=1&txtPsgFlg_2=0&txtPsgFlg_3=0&txtPsgFlg_4=0&txtPsgFlg_5=0&txtPsgFlg_8=0&chkCpn=N&txtSeatAttCd_4=015&txtSeatAttCd_3=000&txtSeatAttCd_2=000&txtGoStartCode2=&txtGoEndCode2=&hidDiscount=&hidEasyTalk=&adjcCheckYn=N"

#정보를 담을 2D 리스트
table_data = []

#10번 반복함.
for _ in range(10):
    #Selenium으로 javascript 실행된 후의 페이지 소스를 가져옴
    driver.get(url)
    wait = WebDriverWait(driver,10)
    html =driver.page_source

    #파싱
    soup = BeautifulSoup(html,'html.parser')

    #페이지를 살펴보니 table안에 tbody부분에 데이터가 들어있음
    #정확히는 tbody안에 tr 행들이 있고, 그 안에 td 데이터들이 들어있음
    #따라서 먼저 tbody를 가져오고, for문으로 tr순회하며 td데이터들을 하나씩 리스트에 담아서 리스트에 저장한다.
    #2D리스트가 되겠다. 이후에 pandas.DataFrame으로 변환해서 가지고 놀 수 있을 것이다.
    #그러나 특실이나 일반실 예매 열은 텍스트가 아닌 이미지로 되어 있다.
    #잘 뜯어보니 td안에 a, img태그 등이 있고, img태그 안에는 alt라는 속성이 있었다.
    #alt안에는 이미지를 설명하는 text가 있었다.
    #따라서 td가 img태그를 갖고 있으면 alt속성의 텍스트를 가져오고 아니면 그냥 텍스트를 가져오자.

    table = soup.find("tbody")
    #tr순회.
    for row in table.find_all("tr"):
        col_data = []
        for td in row.find_all("td"):
            #강의에서는 그냥 텍스트만 추출했지만 본인은 열차의 종류도 궁금하기에 그 부분은 추가했다.
            #열차 종류는 열차번호 부분에 td의 title속성에 들어있다.
            img_tag = td.find_all("img")
            #이미지 태그가 있으면 alt속성 값으로 저장.
            if len(img_tag)!=0:
                text = ""
                for img in img_tag:
                    text += img.get("alt") + "\n"
            #없으면 텍스트 형식이겠다.
            else:
                text = ""
                title = td.get("title")
                if title != None and title != "KTX":
                    text += title
                #여기서는 strip옵션을 사용하기 위해서 get_text메소드를 사용했다.
                #그냥 text로 받게 되면 불필요한 공백이나 \n등도 같이 받아오게 된다.
                text += td.get_text(strip=True)
            col_data.append(text)
        col_data.append(url)
        table_data.append(col_data)

    #'다음' 버튼 찾아서 누르기. XPath를 활용함.
    #XPath는 대충 태그간의 상대적인 주소라고 하는듯 함. 나중에 자세히 공부해봄.
    try:
        next_button = driver.find_element(By.XPATH,"//*[@id=\"divResult\"]/table[2]/tbody/tr/td/a[2]")
    except:
        #다음 버튼을 계속 누르다가 다음 날로 넘어가면 이전 버튼이 사라져서 Xpath가 변경됨. a[2] -> a[1] 그래서 find_element에서 예외 발생하면
        #XPath를 수정한 후 계속 작업을 진행한다.
        #"NoSuchElementException"가 발생함.
        next_button = driver.find_element(By.XPATH,"//*[@id=\"divResult\"]/table[2]/tbody/tr/td/a[1]")
    next_button.click()
    wait = WebDriverWait(driver,10)
    #'다음'버튼을 눌러서 갱신된 url을 변수에 담아준다.
    url = driver.current_url

#할꺼 다했으니 driver는 퇴근한다. 여기서 퇴근하는 이유는 next버튼을 눌러주는 작업을 한 후 퇴근해야 하기 때문이다.
driver.quit()

columns = ["구분","열차 번호", "출발시각", "도착시각", "특실/우등실","일반실","유아","자유석/입석","인터넷특가(멤버십 혜택)","예약 대기","정차역(경유)",
           "차량유형/편성정보","운임 요금","소요 시간", "url"]

table_df = pd.DataFrame(table_data,columns=columns)

#나중에 확인한 사실인데, 코레일 사이트를 잘 보면 페이지의 가장 밑에 위치한 열차정보가 다음 페이지의 가장 맨 위의 열차정보로 들어간다.
#즉, 한 열차가 두 번 중첩되어 저장된다.
#중복을 처리하는 방법이 여러가지가 있겠지만, 여기서는 pandas의 drop_duplicates를 사용하도록 한다.
table_df = table_df.drop_duplicates(subset = ["출발시각","열차 번호","도착시각"], keep ="first")
#subset은 대상 열. 값이 같으면 제거제거!
#제거할 대상 중 남겨두고 싶은 아이는 keep으로 살릴 수 있다.
#keep 에는 first와 last를 할당할 수 있는데, first하면 중복되는 값 중 가장 첫 번째 row를 살리고, last는 가장 마지막 row를 살린다.

#위의 작업으로 인해 row index가 끊어졌으니 리셋해준다.
table_df = table_df.reset_index(drop=True)
#drop파라미터는 기존에 있던 index를 버릴것인지 선택하는 역할이다.
#기본값은 False이다.
#자세한 것은 pandas 쥬피터노트북 문서를 참고하자. (2025.01.31 기준 깃헙에는 아직 안 올림)

table_df.to_csv("csv/06_korail.csv",index=False)
#참고로 한글로 csv를 저장했을때 한글이 깨지면 다음의 스텝을 밟아보자. (엑셀로 열었을 경우임.)
#1. csv파일을 notepad로 열기
#2. 다른 이름으로 저장하기 누르기
#3. 뜨는 창 아래 보면 인코딩이 있는데 UTF-8(BOM)으로 바꾸어보자.(파일을 덮어쓰든지 말든지 그건 자유)
#4. 열어서 한글이 깨지는지 한번 보자.



#부록
#가장 빠른 예약 가능 시각을 알아보자.
#서서가는 것은 싫으니 앉아서 갈 수 있는 것만 가져온다.
fast_reserve_df = table_df[table_df["일반실"]=="예약하기\n좌석선택\n"]
fast_reserve_df = fast_reserve_df.reset_index(drop=True)
#가장 이른 시간을 찾아보자.
print("가장 이른 예약 가능 시간",fast_reserve_df.loc[0,'url'])
fast_reserve_df.to_csv("csv/06_1_korail_fast_reserve.csv",index=False)
                