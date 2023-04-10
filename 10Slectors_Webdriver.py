import time

import action as action
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.maximize_window()

chrome.get("https://formy-project.herokuapp.com/")

chrome.find_element(By.LINK_TEXT, "Enabled and disabled elements").click()

chrome.find_element(By.ID,"input").send_keys("calculator")

chrome.find_element(By.CLASS_NAME,"navbar-brand").click()

chrome.find_element(By.LINK_TEXT,"Checkbox").click()

chrome.find_element(By.ID,"checkbox-2").click()

chrome.back()
chrome.find_element(By.LINK_TEXT,"Autocomplete").click()

chrome.find_element(By.ID,"autocomplete").send_keys("Muntii Godeanu")
address = chrome.find_elements(By.CLASS_NAME,"form-control")
address[1].send_keys("nr 20")
address[3].send_keys("Chinteni")
address[4].send_keys("Cluj")
address[5].send_keys("407205")
address[6].send_keys("Romania")

chrome.back()

chrome.get("https://the-internet.herokuapp.com/")

chrome.find_element(By.LINK_TEXT,"Dynamic Controls").click()
chrome.find_element(By.TAG_NAME,"input").click()

chrome.find_element(By.LINK_TEXT,"Elemental Selenium").click()

chwd = chrome.window_handles
chrome.switch_to.window(chwd[1])

chrome.find_element(By.NAME,"fields[programming_language]").click()

optiuni = chrome.find_elements(By.TAG_NAME,"option")
optiuni[4].click()

chrome.get("http://www.seleniumframework.com/Practiceform/")

chrome.find_element(By.LINK_TEXT,"Browser Commands").click()

chrome.get("https://the-internet.herokuapp.com/")

chrome.find_element(By.LINK_TEXT,"Challenging DOM").click()

word = chrome.find_element(By.XPATH,"//table/tbody/tr[3]/td[4]").text
chrome.back()

chrome.find_element(By.LINK_TEXT,"Form Authentication").click()

chrome.find_element(By.NAME,"username").send_keys(word)

chrome.back()

chrome.find_element(By.PARTIAL_LINK_TEXT,"Chall").click()

chrome.back()

chrome.find_element(By.PARTIAL_LINK_TEXT,"Geo").click()

chrome.find_element(By.TAG_NAME,"button").click()
chrome.back()

chrome.find_element(By.PARTIAL_LINK_TEXT,"Form").click()

chrome.find_element(By.NAME,"username").send_keys("maxim")
chrome.find_element(By.NAME,"password").send_keys("razvan")

chrome.find_element(By.CLASS_NAME,"radius").click()
chrome.get("https://formy-project.herokuapp.com/")

chrome.find_element(By.LINK_TEXT,"Key and Mouse Press").click()

chrome.find_element(By.TAG_NAME,"input").send_keys("THE END!")





