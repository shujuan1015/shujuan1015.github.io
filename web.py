import requests
from bs4 import BeautifulSoup

# 指定網址
url = "https://shujuan1015.github.io/dd.html"

# 發送 GET 請求
response = requests.get(url)
if response.status_code == 200:
    # 使用 BeautifulSoup 解析網頁
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 提取特定內容（例如標題和段落）
    title = soup.title.string
    paragraphs = soup.find_all('p')
    
    # 顯示結果
    print(f"網頁標題: {title}")
    for i, p in enumerate(paragraphs, 1):
        print(f"段落 {i}: {p.get_text()}")
else:
    print(f"無法訪問網頁，狀態碼: {response.status_code}")
