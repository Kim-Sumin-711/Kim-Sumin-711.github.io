import requests
import json

# 서버 URL
url = "http://127.0.0.1:5000/upload"  # Flask 서버 URL

# 업로드할 파일 경로
file_path = "C:/Users/nadda/Desktop/apple.png"

# 파일 전송
with open(file_path, 'rb') as file:
    files = {'file': file}
    response = requests.post(url, files=files)

# 응답 확인
if response.status_code == 200:
    print("File uploaded successfully\n")
else:
    print(f"Failed to upload file: {response.text}\n")


product_id = response.json()
print(json.dumps(product_id,indent=4))


'''url = 'http://127.0.0.1:5000/ID=2'
data = requests.get(url)
a = data.json()
print(json.dumps(a,indent=4))



def asdf(id,url):
    data = requests.get(url+str(id))
    try:    
        a = data.json()
        print(json.dumps(a,indent=4))
    except:
        print("Error")

def fdsa(id,url):
    response = requests.get(url+str(id))
    if response.status_code == 200:
        print(response)
url = 'http://127.0.0.1:5000/history='
url2 = 'http://127.0.0.1:5000/history_image='

asdf(1,url)
fdsa(1,url2)
asdf(2,url)
fdsa(2,url2)
asdf(3,url)
fdsa(3,url2)
asdf(4,url)
fdsa(4,url2)
asdf(5,url)
fdsa(5,url2)
asdf(1,url)
fdsa(1,url2)
asdf(2,url)
fdsa(2,url2)
asdf(3,url)
fdsa(3,url2)
asdf(4,url)
fdsa(4,url2)
asdf(5,url)
fdsa(5,url2)
asdf(1,url)
fdsa(1,url2)
asdf(2,url)
fdsa(2,url2)
asdf(3,url)
fdsa(3,url2)
asdf(4,url)
fdsa(4,url2)
asdf(5,url)
fdsa(5,url2)'''


'''url = 'http://127.0.0.1:5000/history='
def asdfasdf(a):
    
    data = requests.get(f"{url}{a}")
    a = data.json()
    print(json.dumps(a,indent=4))

asdfasdf(1)
asdfasdf(2)
asdfasdf(3)
asdfasdf(4)
asdfasdf(5)
asdfasdf(4)'''
