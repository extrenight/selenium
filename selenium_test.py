#coding = utf-8
import pytest
from selenium import webdriver
from time import sleep, ctime
import os

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
chrome_driver_binary = "D:/Google/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)


class TestCase():
    def setup_method(self):
        driver.get("https://www.baidu.com/")
        sleep(3)

    def teardown_method(self):
        sleep(3)

    def teardown_class(self):
        sleep(3)
        driver.quit()

    def test_one(self):
        driver.find_element_by_id("kw").send_keys("Test search")
        driver.find_element_by_id("su").click()

    def test_two(self):
        driver.find_element_by_id("kw").send_keys("***")
        driver.find_element_by_id("su").click()

    def test_three(self):
        driver.find_element_by_id("kw").send_keys("@")
        driver.find_element_by_id("su").click()

    def test_four(self):
        driver.find_element_by_id("kw").send_keys(" ")
        driver.find_element_by_id("su").click()

    def test_five(self):
        driver.find_element_by_link_text("新闻").click()
