import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tests22(unittest.TestCase):

    NEW_URL = "https://the-internet.herokuapp.com/login"
    ELEMENT = (By.XPATH,'//h2')
    BUTTON = (By.XPATH,'//button')
    LINK_ATTRIBUTE = (By.XPATH,'//div[@id="page-footer"]/div/div/a')
    ERROR = (By.XPATH, '//div[@class="row"]/div/div[@id="flash"]')
    ERROR_MESSAGE = (By.XPATH,'//div[@class="row"]/div/div[@id="flash"]')
    CLOSE_ERROR = (By.XPATH, '//div[@id="flash"]/a')
    SUCCESS = (By.XPATH, '//h2')
    USERNAME = (By.ID,"username")
    PASSWORD = (By.ID, "password")
    CHOOSE_FILE = (By.XPATH, '//input[@type="file"]')
    #CHOOSE_FILE = (By.XPATH, '//input[@id="file-upload"]')
    COOKIES = (By.XPATH,'//div[@class="col-12"]/p/a[@class="_brlbs-btn _brlbs-btn-accept-all _brlbs-cursor"]')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/upload')
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        self.chrome.quit

    def test_upload_CV(self):
        try:
            self.chrome.find_element(*self.COOKIES).click()
        except:
            pass
        self.chrome.find_element(*self.CHOOSE_FILE).send_keys("C:/Users/Maxim/Desktop/Dummy_CV.pdf")
        time.sleep(10)





