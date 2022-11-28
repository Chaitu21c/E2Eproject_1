from selenium import webdriver
from selenium.webdriver.common.by import By
from Library import Configreader
from Base.Initate_Browser import start_browser
import pytest
def test_open_browser():
    driver=start_browser()
    driver.find_element(By.XPATH,Configreader.fetchElement("Registration","username")).send_keys("chaitu123644@gmail.com")
    driver.find_element(By.XPATH,Configreader.fetchElement("Registration","password")).send_keys("00141212")
    driver.find_element(By.XPATH,Configreader.fetchElement("Registration","button")).click()

