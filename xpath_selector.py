import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://the-internet.herokuapp.com/")
chrome.implicitly_wait(5)
chrome.find_element(By.XPATH,"//ul/li[6]/a").click()

chrome.find_element(By.XPATH,"//input[1]").click()
chrome.find_element(By.XPATH,"//input[2]").click()

chrome.back()
chrome.find_element(By.XPATH,"//ul/li[15]/a").click()

chrome.switch_to.active_element.click()

chrome.find_element(By.XPATH,'//*[@id="restart-ad"]').click()

chrome.switch_to.active_element.click()
chrome.back()

chrome.get("https://www.flashscore.ro/")
chrome.find_element(By.XPATH,'//*[@id="my-leagues-list"]/div[1]/div[1]/a/span[2]').click()

chrome.find_element(By.XPATH,'//div[@class="tabs__group"]/a[text()="Rezultate"]').click()

chrome.find_element(By.XPATH,'//div[@class="menuTop__items"]/a[1]/div[text()="Fotbal"]').click()

chrome.find_element(By.XPATH,'//div[@class="calendar__datepicker "]').click()

chrome.find_element(By.XPATH,'//div[@class="calendar__days"]/div[text()="10/12 Sâ"]').click()

chrome.find_element(By.XPATH,'//div[@class="event__header top"]/div[2]/div[1]/span[text()="Cupa Mondială - Play-off"]').click()

chrome.find_element(By.XPATH,'//div[@id="g_1_2g49AZK4"]/div[2]').click()

chwd = chrome.window_handles
chrome.switch_to.window(chwd[1])
chrome.maximize_window()
scor = chrome.find_element(By.XPATH,'//div[@class="duelParticipant"]').text
print(scor)











