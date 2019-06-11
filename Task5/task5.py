#!/usr/bin/env python

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# CASE 1
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
time.sleep(4)
elem = browser.find_element_by_xpath("//html/body/div/div/main/div/div[1]/div[1]/div/section/article[1]/header/div/h3/a").text
print(elem)
elem = browser.find_element_by_xpath("//html/body/div/div/main/div/div[1]/div[1]/div/section/article[1]/div[1]/div[1]/div[2]").text
print(elem)
time.sleep(4)
try:
    browser.find_element_by_tag_name('svg')
except NoSuchElementException:
    print('No icon')
elements = len(browser.find_elements_by_class_name('SearchSegment'))
if elements < 5:
    print('False')
browser.quit()

# CASE 2
browser = webdriver.Firefox()
browser.get('https://rasp.yandex.ru')
elem = browser.find_element_by_id('from')
elem.clear()
time.sleep(2)
elem.send_keys('Кемерово проспект Ленина')
elem = browser.find_element_by_id('to')
elem.send_keys('Кемерово Бакинский переулок')
elem = browser.find_element_by_id('when')
elem.send_keys('среда')
bus = browser.find_element_by_xpath(
    '//*[@id="root"]/div/header/div[1]/div/div[4]/span/label[5]')
bus.click()
time.sleep(2)
button = browser.find_element_by_xpath('//*[@id="root"]/div/header/div[1]/div/div[5]/form/button[2]')
button.click()
try:
    browser.find_elements_by_class_name('ErrorPage')
except NoSuchElementException:
    print('No error page')
