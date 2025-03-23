from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re
from selenium.webdriver.support.ui import WebDriverWait


#크롤링 할때는 전체화면 키고 하자. 안그러면 짤린 elem들을 가져오지 않을 때가 있다.
img_save_file = "C:/Users/nadda/Desktop/sw/github/Kim-Sumin-711.github.io/Flask/Flask_Test_for_24-2H_DT/static/Img/"


driver = webdriver.Chrome()
'''driver.get("file:///C:/Users/nadda/Desktop/sw/github/Kim-Sumin-711.github.io/Flask/Flask_Test_for_24-2H_DT/static/CU_htmls/CU_instant.mhtml")

time.sleep(3)

item_img = []
item_name = []
item_promotion = []
item_price = []


item_container = driver.find_elements(By.CLASS_NAME,"prod_list")



for item in item_container:
    img = item.find_element(By.CLASS_NAME,"prod_img").find_element(By.TAG_NAME,"img")
    name = item.find_element(By.CLASS_NAME,"name")
    price = item.find_element(By.CLASS_NAME,"price")
    promotion = item.find_element(By.CLASS_NAME,"badge")
    item_img.append(img)
    item_name.append(name)
    item_price.append(price)
    item_promotion.append(promotion)

id = 0
with open("static/img_path.csv","w",encoding='UTF-8') as img_file:
    for Img in item_img:
        id+=1
        path = Img.get_attribute("alt")
        img_file.write(f"{id},{img_save_file+path}\n")

id = 0
with open("static/product_info.csv","w",encoding='UTF-8') as info_file:
    for i in range(len(item_name)):
            id+=1
            info_file.write(f"{id},{item_name[i].find_element(By.TAG_NAME, 'p').text},{item_price[i].find_element(By.TAG_NAME, 'strong').text.replace(",","")}")
            try:
                tmp = item_promotion[i].find_element(By.TAG_NAME, 'span')
                tmp_txt = tmp.text
                info_file.write(f",{tmp_txt}\n")
            except:
                info_file.write(f",Nothing\n")


#=======================================================================

driver.get("file:///C:/Users/nadda/Desktop/sw/github/Kim-Sumin-711.github.io/Flask/Flask_Test_for_24-2H_DT/static/CU_htmls/CU_simple.mhtml")

time.sleep(3)

item_img = []
item_name = []
item_promotion = []
item_price = []


item_container = driver.find_elements(By.CLASS_NAME,"prod_list")



for item in item_container:
    img = item.find_element(By.CLASS_NAME,"prod_img").find_element(By.TAG_NAME,"img")
    name = item.find_element(By.CLASS_NAME,"name")
    price = item.find_element(By.CLASS_NAME,"price")
    promotion = item.find_element(By.CLASS_NAME,"badge")
    item_img.append(img)
    item_name.append(name)
    item_price.append(price)
    item_promotion.append(promotion)

id = 124
with open("static/img_path.csv","a",encoding='UTF-8') as img_file:
    for Img in item_img:
        id+=1
        path = Img.get_attribute("alt")
        img_file.write(f"{id},{img_save_file+path}\n")

id = 124
with open("static/product_info.csv","a",encoding='UTF-8') as info_file:
    for i in range(len(item_name)):
        id+=1
        info_file.write(f"{id},{item_name[i].find_element(By.TAG_NAME, 'p').text},{item_price[i].find_element(By.TAG_NAME, 'strong').text.replace(",","")}")
        try:
            info_file.write(f",{item_promotion.find_element(By.TAG_NAME, 'span').text}\n")
        except:
            info_file.write(f",Nothing\n")

#======================================================

driver.get("file:///C:/Users/nadda/Desktop/sw/github/Kim-Sumin-711.github.io/Flask/Flask_Test_for_24-2H_DT/static/CU_htmls/CU_snacks.mhtml")

time.sleep(3)

item_img = []
item_name = []
item_promotion = []
item_price = []


item_container = driver.find_elements(By.CLASS_NAME,"prod_list")



for item in item_container:
    img = item.find_element(By.CLASS_NAME,"prod_img").find_element(By.TAG_NAME,"img")
    name = item.find_element(By.CLASS_NAME,"name")
    price = item.find_element(By.CLASS_NAME,"price")
    promotion = item.find_element(By.CLASS_NAME,"badge")
    item_img.append(img)
    item_name.append(name)
    item_price.append(price)
    item_promotion.append(promotion)

id = 473
with open("static/img_path.csv","a",encoding='UTF-8') as img_file:
    for Img in item_img:
        id+=1
        path = Img.get_attribute("alt")
        img_file.write(f"{id},{img_save_file+path}\n")

id = 473
with open("static/product_info.csv","a",encoding='UTF-8') as info_file:
    for i in range(len(item_name)):
        id+=1
        info_file.write(f"{id},{item_name[i].find_element(By.TAG_NAME, 'p').text},{item_price[i].find_element(By.TAG_NAME, 'strong').text.replace(",","")}")
        try:
            info_file.write(f",{item_promotion.find_element(By.TAG_NAME, 'span').text}\n")
        except:
            info_file.write(f",Nothing\n")'''


#===================================================

'''driver.get("file:///C:/Users/nadda/Desktop/sw/github/Kim-Sumin-711.github.io/Flask/Flask_Test_for_24-2H_DT/static/CU_htmls/CU_icecream.mhtml")

time.sleep(3)

item_img = []
item_name = []
item_promotion = []
item_price = []


item_container = driver.find_elements(By.CLASS_NAME,"prod_list")



for item in item_container:
    img = item.find_element(By.CLASS_NAME,"prod_img").find_element(By.TAG_NAME,"img")
    name = item.find_element(By.CLASS_NAME,"name")
    price = item.find_element(By.CLASS_NAME,"price")
    promotion = item.find_element(By.CLASS_NAME,"badge")
    item_img.append(img)
    item_name.append(name)
    item_price.append(price)
    item_promotion.append(promotion)

id = 2512

with open("static/img_path.csv","a",encoding='UTF-8') as img_file:
    for Img in item_img:
        id+=1
        path = Img.get_attribute("alt")
        img_file.write(f"{id},{img_save_file+path}\n")

id = 2512
with open("static/product_info.csv","a",encoding='UTF-8') as info_file:
    for i in range(len(item_name)):
        id+=1
        info_file.write(f"{id},{item_name[i].find_element(By.TAG_NAME, 'p').text},{item_price[i].find_element(By.TAG_NAME, 'strong').text.replace(",","")}")
        try:
            info_file.write(f",{item_promotion.find_element(By.TAG_NAME, 'span').text}\n")
        except:
            info_file.write(f",Nothing\n")'''

#=============================

'''driver.get("file:///C:/Users/nadda/Desktop/sw/github/Kim-Sumin-711.github.io/Flask/Flask_Test_for_24-2H_DT/static/CU_htmls/CU_food.mhtml")

time.sleep(3)

item_img = []
item_name = []
item_promotion = []
item_price = []


item_container = driver.find_elements(By.CLASS_NAME,"prod_list")



for item in item_container:
    img = item.find_element(By.CLASS_NAME,"prod_img").find_element(By.TAG_NAME,"img")
    name = item.find_element(By.CLASS_NAME,"name")
    price = item.find_element(By.CLASS_NAME,"price")
    promotion = item.find_element(By.CLASS_NAME,"badge")
    item_img.append(img)
    item_name.append(name)
    item_price.append(price)
    item_promotion.append(promotion)

id = 2940

with open("static/img_path.csv","a",encoding='UTF-8') as img_file:
    for Img in item_img:
        id+=1
        path = Img.get_attribute("alt")
        img_file.write(f"{id},{img_save_file+path}\n")

id = 2940
with open("static/product_info.csv","a",encoding='UTF-8') as info_file:
    for i in range(len(item_name)):
        id+=1
        info_file.write(f"{id},{item_name[i].find_element(By.TAG_NAME, 'p').text},{item_price[i].find_element(By.TAG_NAME, 'strong').text.replace(",","")}")
        try:
            info_file.write(f",{item_promotion.find_element(By.TAG_NAME, 'span').text}\n")
        except:
            info_file.write(f",Nothing\n")'''

#=============================
'''driver.get("file:///C:/Users/nadda/Desktop/sw/github/Kim-Sumin-711.github.io/Flask/Flask_Test_for_24-2H_DT/static/CU_htmls/CU_drink.mhtml")

time.sleep(3)

item_img = []
item_name = []
item_promotion = []
item_price = []


item_container = driver.find_elements(By.CLASS_NAME,"prod_list")



for item in item_container:
    img = item.find_element(By.CLASS_NAME,"prod_img").find_element(By.TAG_NAME,"img")
    name = item.find_element(By.CLASS_NAME,"name")
    price = item.find_element(By.CLASS_NAME,"price")
    promotion = item.find_element(By.CLASS_NAME,"badge")
    item_img.append(img)
    item_name.append(name)
    item_price.append(price)
    item_promotion.append(promotion)

id = 6127

with open("static/img_path.csv","a",encoding='UTF-8') as img_file:
    for Img in item_img:
        id+=1
        path = Img.get_attribute("alt")
        img_file.write(f"{id},{img_save_file+path}\n")

id = 6127
with open("static/product_info.csv","a",encoding='UTF-8') as info_file:
    for i in range(len(item_name)):
        id+=1
        info_file.write(f"{id},{item_name[i].find_element(By.TAG_NAME, 'p').text},{item_price[i].find_element(By.TAG_NAME, 'strong').text.replace(",","")}")
        try:
            info_file.write(f",{item_promotion.find_element(By.TAG_NAME, 'span').text}\n")
        except:
            info_file.write(f",Nothing\n")'''

#=======================

driver.get("file:///C:/Users/nadda/Desktop/sw/github/Kim-Sumin-711.github.io/Flask/Flask_Test_for_24-2H_DT/static/CU_htmls/CU_others.mhtml")

time.sleep(3)

item_img = []
item_name = []
item_promotion = []
item_price = []


item_container = driver.find_elements(By.CLASS_NAME,"prod_list")



for item in item_container:
    img = item.find_element(By.CLASS_NAME,"prod_img").find_element(By.TAG_NAME,"img")
    name = item.find_element(By.CLASS_NAME,"name")
    price = item.find_element(By.CLASS_NAME,"price")
    promotion = item.find_element(By.CLASS_NAME,"badge")
    item_img.append(img)
    item_name.append(name)
    item_price.append(price)
    item_promotion.append(promotion)

id = 7420
with open("static/img_path.csv","a",encoding='UTF-8') as img_file:
    for Img in item_img:
        id+=1
        path = Img.get_attribute("alt")
        img_file.write(f"{id},{img_save_file+path}\n")

id = 7420
with open("static/product_info.csv","a",encoding='UTF-8') as info_file:
    for i in range(len(item_name)):
        id+=1
        info_file.write(f"{id},{item_name[i].find_element(By.TAG_NAME, 'p').text},{item_price[i].find_element(By.TAG_NAME, 'strong').text.replace(",","")}")
        try:
            info_file.write(f",{item_promotion.find_element(By.TAG_NAME, 'span').text}\n")
        except:
            info_file.write(f",Nothing\n")

print("end")