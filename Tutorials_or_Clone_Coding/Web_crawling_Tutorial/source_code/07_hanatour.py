#하나투어 관광상품 리뷰 분석
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.hanatour.com/trp/pkg/CHPC0PKG0200M200?pkgCd=JOP131250303RSD&prePage=major-products"
driver.get(url)


#여행후기를 클릭한다.
#review_link = driver.find_element(By.XPATH, "//*[@id=\"sticky06-bottom\"]")
#클릭하고싶은 버튼이 뜰 때 까지 기다린 후에 찾고 클릭한다.
#파라미터 튜플로 주는거 조심.
review_link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"sticky06-bottom\"]")))
review_link.click()
time.sleep(2)

reviews = []
#페이지네이션
for page_num in range(1,200):
    #페이지 번호 뜨는 div부분이 로딩될때까지 기다림.
    paginate_div = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"paginate")))
    #현재 페이지를 출력한다.
    print("현재 페이지 : ",page_num)
    #리뷰를 담은 리뷰 상자들은 ul태그 밑의 li태그속에 하나씩 담겨있다.
    #이 친구들을 이번에는 CSS_Selector로 찾아본다.
    ##sticky06 > div > div.rating_list > ul > li:nth-child(1)
    #위는 CSS_Selector의 예시이다. 경로를 나타냄.
    #. 뒤는 클래스 이름인 것 같다. nth-child 1번째 자식?인 li를 나타내는 경로이다.

    lis = driver.find_elements(By.CSS_SELECTOR, "ul.list_review_v2 > li")
    #ul태그 중 list_review_v2라는 클래스 소속인 태그를 찾은 후
    #자식 태그들 중에 li를 find_elements로 전부 가져온다.
    for li in lis:
        #하나의 리뷰를 저장할 딕셔너리
        review_info = {}
        rating_info = li.find_element(By.CLASS_NAME,"rating_info")

        #별점
        rating = rating_info.find_element(By.TAG_NAME,'strong').text if rating_info.find_element(By.TAG_NAME,'strong') else ""
        review_info["Rating"]= rating

        #span
        spans = rating_info.find_elements(By.TAG_NAME,"span")
        review_info['User'] = spans[1].text
        review_info['Category'] = spans[2].text
        review_info["Age"] = spans[3].text
        review_info["Date"] = spans[-1].text

        #review추출
        #class name으로 찾을 때 class name에 공백이 있고, 뭐가 이어져 있으면 공백 전까지만 입력하자
        #review_cont con인데 저걸 다 입력하면 NoSuchElementException이 뜬다.
        review = li.find_element(By.CLASS_NAME,"review_cont")
        review_text =  review.text if review else ""
        review_info["Review"]=review.text

        #리뷰 카테고리
        review_cate = li.find_element(By.CLASS_NAME,"review_cate")
        review_cate_text = review_cate.text if review_cate else ""
        review_info["Review_cate"] = review_cate_text

        reviews.append(review_info)
    #다음 페이지로 이동.
    try:
        #페이지가 1~9, 11~19, 21~29
        if page_num%10!=0:
            #현제 페이지 넘버+1인 버튼을 찾는다. 여기서 XPath가 간결한 이유는 이미 pagenate_div에
            #도달한 상태에서 찾기에 그 앞의 정보는 필요없기 때문이다. (모르겠으면 그냥 전부 복붙해도 된다.)
            #저기서 text()=페이저넘+1 은 a태그인데 text로 페이지넘+1을 갖고 있는 아이를 추가하겠다는 의미.
            next_link = paginate_div.find_element(By.XPATH, f"//span/a[text()='{page_num+1}']")
            next_link.click()
        else:
            next_link=paginate_div.find_element(By.XPATH,"//*[@id=\"sticky06\"]/div/div[4]/div[3]/div/div/a[3]")
            next_link.click()
        time.sleep(2)
    except:
        #다음버튼이나 숫자버튼 못찾았을 경우. 이 경우는 마지막 페이지인 경우이다.
        print("마지막 페이지에 도달하였습니다.")
        break
#종료
driver.quit()

reviews_df = pd.DataFrame(reviews)
reviews_df.to_csv("csv/07_hanatour.csv",index=False)