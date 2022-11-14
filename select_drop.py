from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
import time

s = Service('C:/webdr/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=s, options=options)
url = 'https://www.moex.com/ru/derivatives/currency-rate.aspx?currency=USD_RUB'
driver.get(url)
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="content_disclaimer"]/div/div/div/div[1]/div/a[1]').click()
drop_currency = driver.find_element(By.XPATH, '//*[@id="ctl00_PageContent_CurrencySelect"]')
begin_day = driver.find_element(By.XPATH, '//*[@id="d1day"]')
begin_month = driver.find_element(By.XPATH, '//*[@id="d1month"]')
b_d = Select(begin_day)
time.sleep(1)
b_d.select_by_index(0)
b_d.select_by_value("1")
b_m = Select(begin_month)
b_m.select_by_index(1)
Select(driver.find_element(By.XPATH, '//*[@id="d1day"]')).select_by_value("1")


b_m.select_by_value("10")


time.sleep(10)