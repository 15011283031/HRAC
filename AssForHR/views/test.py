# 模拟驱动
from selenium import webdriver
import unittest, time#延时用

# django的http驱动
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

#beautiful 用于解析网页
import bs4 as bs


def createDriver():
    """
    create firefox webdriver
    """
    firefox_driver = webdriver.Firefox()
    url_std = 'http://mail.yooli.com'
    firefox_driver.get(url_std)
    time.sleep(2)
    firefox_driver.find_element_by_id('qquin').send_keys('yongqiang.chen')
    firefox_driver.find_element_by_id('pp').send_keys('y0729301613Q')
    time.sleep(2)
    firefox_driver.find_element_by_class_name('login_btn').click()
    time.sleep(2)
    return firefox_driver


firefox_driver = createDriver()




