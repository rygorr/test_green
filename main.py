from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
s = Service('C:/webdr/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
url = 'https://www.moex.com/'
driver.get(url)
time.sleep(2)
driver.find_element(By.CLASS_NAME, "header-nav__mobile-menu-button").click()
time.sleep(1)
derivative = driver.find_element(By.LINK_TEXT, 'Срочный рынок')
derivative.click()
# принятие соглашения
try:
    driver.find_element(By.XPATH, '//*[@id="content_disclaimer"]/div/div/div/div[1]/div/a[1]').click()
except Exception:
    print('Соглашение уже принято')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ctl00_frmLeftMenuWrap"]/div/div/div[2]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="ctl00_frmLeftMenuWrap"]/div/div/div[3]/div[13]/div').click()
time.sleep(5)
#дошел до нужной страницы