from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\webdriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
action = webdriver.ActionChains(driver)
driver.get("https://www.ebay.com/")
driver.maximize_window()
time.sleep(5)
link = driver.find_element_by_xpath ("/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[1]/div/div/input[1]")
link.send_keys("SmartPhone")
time.sleep(3)
select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "gh-cat"))))
select.select_by_visible_text("Music")
link = driver.find_element_by_xpath ("/html/body/header/table/tbody/tr/td[3]/form/table/tbody/tr/td[3]/input")
link.click()