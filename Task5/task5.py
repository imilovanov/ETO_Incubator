#!/usr/bin/env python

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://rasp.yandex.ru')

elem = browser.find_element_by_id('from')
elem.send_keys('Кемерово')
time.sleep(1)
elem = browser.find_element_by_id('to')
elem.send_keys('Москва')
elem.send_keys(Keys.ENTER)
time.sleep(1)
