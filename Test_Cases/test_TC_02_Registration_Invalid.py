from selenium.webdriver.common.by import By
from Library import Configreader
from Base.Initate_Browser import start_browser

def test_Registration():
    browser=start_browser()
    #print("\nTest Registration called")
    driver =Configreader.readconfigData("Details","Application_url")
    driver.find_element(By.XPATH, Configreader.fetchElement("Registration", "username")).send_keys("Samrata@gmail.com")
    driver.find_element(By.XPATH, Configreader.fetchElement("Registration", "password")).send_keys("samrata@1234")
    driver.find_element(By.XPATH, Configreader.fetchElement("Registration", "button")).click()
    msg = driver.find_element(By.XPATH, Configreader.fetchElement("WelcomePage", "errormsg")).text
    assert 'Invalid login or password' in msg
