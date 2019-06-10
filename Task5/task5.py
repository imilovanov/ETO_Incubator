#!/usr/bin/env python

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://rasp.yandex.ru')

elem = browser.find_element_by_id('from')
elem.clear()
elem.send_keys('Кемерово')
time.sleep(1)
elem = browser.find_element_by_id('to')
elem.send_keys('Москва')
elem = browser.find_element_by_id('when')
elem.send_keys('7 июля')
elem.send_keys(Keys.ENTER)
time.sleep(2)
elem = browser.find_element_by_xpath("//html/body/div/div/main/div/div[1]/div[1]/div/section/article[1]/header/div/h3/a")
print(elem)
elem = browser.find_element_by_xpath("//html/body/div/div/main/div/div[1]/div[1]/div/section/article[1]/div[1]/div[1]/div[2]").text
print(elem)
time.sleep(2)
