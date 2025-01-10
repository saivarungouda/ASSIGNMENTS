import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge("C:/Drivers/edgedriver_win64/msedgedriver.exe")

driver.maximize_window()
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "//*[@id='user-name']").send_keys("saivarungoud26@gmail.com")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("9866400626")
driver.find_element(By.XPATH, "//*[@id='login-button']").click()
time.sleep(4)
driver.close()