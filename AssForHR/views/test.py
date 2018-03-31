from selenium import webdriver
import bs4 as bs

driver = webdriver.Firefox()
url='http://mail.yooli.com'
driver.get(url)
driver.close

