from selenium import webdriver
global driver
def start_browser():
    driver=webdriver.Chrome(executable_path="chromedriver.exe")
    driver.get("https://www.instagram.com/p/Ck72yRtJHRg/")
    driver.maximize_window()
    return driver
def close_browser():
    driver.close_window()
