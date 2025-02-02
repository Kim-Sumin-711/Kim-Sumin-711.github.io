#RSS(Really Simple Syndication)란 웹 사이트에서 컨텐츠를 사용자에게 쉽게 배포하기 위한 표준 포멧이다.
#RSS를 사용하면 사용자는 해당 웹 사이트를 방문하지 않아도 해당 사이트의 업데이트된 내용을 확인할 수 있기 떄문에,
#지금 필자가 하고 있는 크롤링(스크랩)과 유사하지만 훨씬 쉽다고 할 수 있다.
#RSS는 사용자가 관심 있는 웹 사이트의 업데이트를 받아보고자 할 때 사용되는 것이고,
#크롤링은 웹 사이트의 데이터를 자동으로 수집하고 분석하기 위해 사용한다.
#목적과 방법에서 차이가 있지만, 둘 다 웹 콘텐츠를 가져오는 데 사용되는 방법이다.

#pip install feedparser
import pandas as pd
import feedparser

#rss사이트는 sbs rss사이트의 정치 카테고리를 이용한다.
url = "https://news.sbs.co.kr/news/SectionRssFeed.do?sectionId=01&plink=RSSREADER"
feed = feedparser.parse(url)
#print(feed)
#살펴보면 summary, title, authors, tags, 날짜 등 여러 정보들이 들어있음.

#피드 항목들을 순회하며 정보 출력
'''print("Feed Title:",feed.feed.title)
for entry in feed.entries:
    print("Title:", entry.title)
    print("url:",entry.link)
    print("Date:",entry.published)
    print("Summary:",entry.summary)
    print("\n")'''

#빈 리스트 정의
url_list = []
title_list = []
summary_list = []
date_list = []

#feed entries순회하며 정보 저장
for entry in feed.entries:
    url_list.append(entry.link)
    title_list.append(entry.title)
    summary_list.append(entry.summary)
    date_list.append(entry.published)

data = {"뉴스url":url_list, "제목":title_list, "내용요약":summary_list,"날짜":date_list}
df = pd.DataFrame(data)
df.to_csv("csv/05_sbs_rss.csv",index=False)