import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument('--kiosk')
chrome_options = webdriver.ChromeOptions()
service = Service(r"/Users/pkc/.wdm/drivers/chromedriver/mac64/96.0.4664.45/chromedriver")
url = "https://play.google.com/store/apps/details?id=kr.co.thejoin.healthnyou.seoul&showAllReviews=true"

driver = webdriver.Chrome(service=service)
driver.get(url)

last_height = driver.execute_script("return document.body.scrollHeight")

SCROLL_PAUSE_TIME = 2
SCROLL_TIMES = 4
CLICK_PAUSE_TIME = 2

while True:
    for i in range(SCROLL_TIMES):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return document.body.scrollHeight")
    
    if new_height == last_height:
        break
    
    last_height = new_height
