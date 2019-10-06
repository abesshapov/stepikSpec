import time
from math import sin, log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )     
    browser.find_element_by_id("book").click()
    button = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    x = int(browser.find_element_by_id("input_value").text)
    res = str(log(abs(12*sin(x))))
    browser.find_element_by_id("answer").send_keys(res)
    xp = '//button[contains(text(), "Submit")]'
    button = browser.find_element_by_xpath(xp)
    button.click()        
    a = browser.switch_to.alert
    print(a.text)
finally:
    time.sleep(5)
    browser.quit()