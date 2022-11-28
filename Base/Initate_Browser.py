from selenium import webdriver
global driver
from Library import Configreader
def start_browser():
    global driver
    browser=Configreader.readconfigData('Details','Browser')
    print(browser)
    if browser=="Chrome":
        driver=webdriver.Chrome(executable_path="chromedriver.exe")
    elif browser=="Firefox":
        driver = webdriver.Firefox(executable_path="geckodriver.exe")
    driver.get(Configreader.readconfigData('Details','Application_url'))
    driver.maximize_window()
    return driver

#def close_browser():
 #   driver.close_window()
