# -*- coding: utf-8 -*-
"""2022.112.2_ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_nYD10i4fa0wE80d_iCjuQp0xFHdJaXI
"""

print('Hello World')

# !pip install selenium
# !apt-get update
# !apt install chromium-chromedriver
# !cp /usr/lib/chromium-browser/chromedriver/usr/bin

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver_path = "2022.12.2_scraping/chromedriver.exe"
# webdriverの作成
service = Service(executable_path=driver_path) # 2) executable_pathを指定
driver = webdriver.Chrome(service=service) # 3) serviceを渡す
# browser = webdriver.Chrome('chromedriver.exe')

from selenium.webdriver.common.by import By
# pythonによる情報取得でよく使われるライブラリBeautiful soup
from bs4 import BeautifulSoup
import time

html = "<body><h1>スクレイピング</h1></body>"
soup = BeautifulSoup(html,"html.parser")
print(soup.h1.text)

#Google Colab 特有の設定
options = webdriver.ChromeOptions()

#Brower をHeadlessモード
options.add_argument('--headless')

#サンドボックスの解除
options.add_argument('--no-sandbox')

options.add_argument('--disable-dev-shm-usage')

# サイトから情報取得

# インスタンス化
driver = webdriver.Chrome('chromedriver',options=options)

# ドライバーを探す時間を確保
driver.implicitly_wait(10)

# 取得するページのURL指定
url="https://club-tullys.jp/login"

driver.get(url)
time.sleep(3)

print(driver.title)

login = "fujiihyrk@gmail.com"
password = "fujkan1120"

# user name自動入力
driver.find_element(By.XPATH,"//*[@id='contentForm']/form/table/tbody/tr[1]/td/input").send_keys(login)
driver.find_element(By.XPATH,"//*[@id='contentForm']/form/table/tbody/tr[2]/td/input").send_keys(password)

#ログインボタンを押す
driver.find_element(By.XPATH,"//*[@id='contentFormBtn']").click()
time.sleep(5)

#見えるようにする

html= driver.page_source
soup = BeautifulSoup(html,"lxml")
content = soup.select('#contentInfo02')
login_user = soup.select('.msg')
copyright = soup.select('#Copyright')
print(soup)

#CSVへの書き出し
# CSVモジュールのインポート
import csv

data = [copyright,content]
f = open('out.csv','w', encoding="utf-8_sig")
writer = csv.writer(f)
writer.writerow(data)
f.close()