#!/usr/bin/env python
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class SchedulePage(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get("https://rasp.yandex.ru")

    def test1(self):
        time.sleep(1)
        self._from = self.browser.find_element_by_id("from")
        self._to = self.browser.find_element_by_id("to")
        self._when = self.browser.find_element_by_id("when")
        self._from.clear()
        self._from.send_keys("Кемерово")
        self._to.send_keys("Москва")
        self._when.send_keys("7 июля")
        self._when.send_keys(Keys.ENTER)        
        time.sleep(2)
        print("TEST 1:")
        try:
            self.header = self.browser.find_element_by_xpath("//html/body/div/div/main/div/div[1]/div[1]/div/section/article[1]/header/div/h3/a")
            print("Header is displayed: " + self.header.text)
        except NoSuchElementException:
            print("No header")
        time.sleep(2)
        try:
            self.duration = self.browser.find_element_by_xpath("//html/body/div/div/main/div/div[1]/div[1]/div/section/article[1]/div[1]/div[1]/div[2]")
            print("Duration time is displayed: " + self.duration.text)
        except NoSuchElementException:
            print("No duration time")
        try:
            self.browser.find_element_by_tag_name("svg")
            print("Icon is displayed")
        except NoSuchElementException:
            print("No icon")

        search_segment = self.browser.find_elements_by_class_name("SearchSegment")
        segments = len(search_segment)
        if segments == 5:
            print("5 segments")
        else:
            print("Not 5 segments")

    def test2(self):
        self._from = self.browser.find_element_by_id("from")
        self._from.clear()
        self._from.send_keys("Кемерово проспект Ленина")
        self._to = self.browser.find_element_by_id("to")
        self._to.send_keys("Кемерово Бакинский переулок")
        self._when = self.browser.find_element_by_id("when")
        self._when.send_keys("среда")
        print("TEST 2:")
        bus = self.browser.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div/div[4]/span/label[5]")
        bus.click()
        search_button = self.browser.find_element_by_xpath("//*[@id='root']/div/header/div[1]/div/div[5]/form/button[2]")
        search_button.click()
        try:
            self.browser.find_elements_by_class_name("ErrorPage")
            print("Error page is displayed")
        except NoSuchElementException:
            print("No error page")

if __name__ == "main":
    unittest.main()
