from bs4 import BeautifulSoup

html_doc = '''
<!DOCTYPE html>
<html>
<head>
    <title>마인크래프트 무료 다운</title>
</head>
<body>
    <h1>마인크래프트 무료 다운로드하는 방법</h1>
    <h2>정품, 불법X, 무료, 바이러스 X</h2>
    <p>1.구글에 "마인크래프트 무료 다운로드 1.9.2 APK" 검색하기</p>
    <p>2.구글 검색 5페이지로 넘어가서 4번째 게시물 클릭하기</p>
    <p>3.다운로드 버튼 누르고 압축 해제하기.</p>
    <p>4.exe파일 실행시키기</p>
</body>
</html>'''

soup = BeautifulSoup(html_doc, 'html.parser')
#파싱해서 간단하게 추출.

#변수에 각 elem담기
title = soup.title
heading1 = soup.h1
paragraph = soup.p

#<title> 부터 </title>까지 다 가져옴
print(title)

#<title>과 </title> 사이의 텍스트만 가져옴
print(title.text)

print(paragraph)
#이러면 가장 먼저 발견된 p 가져옴.

paragraph_all = soup.find_all('p')
print(paragraph_all)
#이러면 p태그를 가진 모든 아이들을 리스트에 담아서 반환
#여기서 바로 paragraph_all.text하면 안됨.
#리스트니까, 각 elem을 순회하면서 text를 사용하자.

for p in paragraph_all:
    print(p.text)

#주의사항
#웹사이트를 크롤링할때 /robots.txt 를 확인하자.
#거기에는 크롤링을 어디까지 허용할 지 적혀있는데
#간과하면 문제가 발생할지도 모른다.
# 
#disallow / 하면 모든 페이지는 크롤링 하면 안됨.
#allow /$ 이면 첫 페이지만 허용.
# https://namu.wiki/w/robots.txt
