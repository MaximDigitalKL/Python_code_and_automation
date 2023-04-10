import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/")
chrome.implicitly_wait(5)
chrome.find_element(By.LINK_TEXT,"Form Authentication").click()
chrome.find_element(By.CSS_SELECTOR,"#username").send_keys("tomsmith")
chrome.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys("SuperSecretPassword!")
chrome.find_element(By.CSS_SELECTOR,'.radius').click()

