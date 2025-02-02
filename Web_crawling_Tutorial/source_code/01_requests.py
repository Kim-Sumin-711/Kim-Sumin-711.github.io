import requests

url = "https://www.google.com"
response = requests.get(url)
print(f"상태 코드: {response.status_code}")
print(f"헤더 정보: {response.headers}")
print(f"HTML 내용: {response.text}")

#200 : ok
#404 : 없음
#400 : bad request 권한 없거나 등등

