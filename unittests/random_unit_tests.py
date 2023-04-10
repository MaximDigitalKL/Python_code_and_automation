import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Tests1(unittest.TestCase):

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


    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(By.LINK_TEXT,'Form Authentication').click()
        self.chrome.implicitly_wait(3)

    def tearDown(self) -> None:
        self.chrome.quit

#- Verify new URL is correct
    def test_The_Correct_URL(self):
        actual_url = self.chrome.current_url
        assert self.NEW_URL == actual_url, "Error, Invalid URL"

#- Verifică if page title is correct
    def test_Verify_Page_Title(self):
        assert self.chrome.title == "The Internet", f'Error, invalid Page Title!'

#- Verify if text from element xpath=//h2 is correct
    def test_xpath_element(self):
        expected_text = "Login Page"
        actual_text = self.chrome.find_element(*self.ELEMENT).text
        assert expected_text == actual_text, f'Error, expected text {expected_text},' \
                                             f'retrieved text {actual_text}'
#- Verify if Login Button is displayed
    def test_login_button(self):
        assert self.chrome.find_element(*self.BUTTON).is_displayed() == True, f'Error, "Login Button" is not displayed'

#- Verify if atribute of href link 'Elemental Selenium' is correct
    def test_Elemental_Selenium(self):
        attribute = self.chrome.find_element(*self.LINK_ATTRIBUTE)
        assert hasattr(attribute,'_parent') == True, 'Error, invalid attribute'

#- Leave user and pass empty, press login, verify if error is displayed
    def test_login_without_credentials(self):
        self.chrome.find_element(*self.BUTTON).click()
        assert self.chrome.find_element(*self.ERROR).is_displayed() == True, 'Error, Alert is not displayed'

#- Fill in invalid user and pass, press login, verify if error message is correct
    def test_error_message(self):
        self.chrome.find_element(By.ID, 'username').send_keys('Jimmy')
        self.chrome.find_element(By.ID, 'password').send_keys('Boy')
        self.chrome.find_element(*self.BUTTON).click()
        expected_message = "Your username is invalid"
        actual_message = self.chrome.find_element(*self.ERROR_MESSAGE).text
        self.assertTrue(expected_message in actual_message, 'Error message is incorrect')

# - Leave user and pass empty, press login, press "x" on the error, check if the error has dissapeared
    def test_close_allert(self):
        self.chrome.find_element(*self.BUTTON).click()
        self.chrome.find_element(*self.CLOSE_ERROR).click()
        try:
            self.chrome.find_element(*self.ERROR)
        except:
            print('Error is no longer displayed')


# - Take all //label as a list, verify each label text to be the ones expected (Username/ Password)
    def test_label_text(self):
        list = self.chrome.find_elements(By.XPATH,'//label')
        first_text = list[0].text
        assert first_text == "Username", f'Error, expected Username, retrieved {first_text}'
        second_text = list[1].text
        assert second_text == "Password", f'Error, expected Password, retrieved {second_text}'

#- Fill in valid user and pass, press login, verify new URL contains "secure".
    # Use explicit wait for element with class "flash success"
    # Verify if the element is dispalyed
    def test_validation(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.BUTTON).click()
        url = self.chrome.current_url
        self.assertTrue("secure" in url, 'Error, "secure" is not in URL')
        confirmation_element = WebDriverWait(self.chrome,1).until(EC.presence_of_element_located((By.XPATH,'//div[@class="flash success"]')))
        assert confirmation_element.is_displayed() == True, f'Error, the element is not displayed'

# -Fill in valid user and pass, click login, click logout, verify is URL is: https://the-internet.herokuapp.com/login
    def test_return_validation(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.BUTTON).click()
        self.chrome.find_element(By.XPATH,'//a[@class="button secondary radius"]').click()
        assert self.chrome.current_url == "https://the-internet.herokuapp.com/login", 'Error, invalid URL'

#-Brute force password hacking (consider each word of element //h4 a password)
    def test_brute_force_hacking(self):
        pass_list = self.chrome.find_element(By.XPATH, '//h4').text.split()
        P_found = False
        for word in pass_list:
            self.chrome.find_element(*self.USERNAME).send_keys('tomsmith')
            self.chrome.find_element(*self.PASSWORD).send_keys(word)
            self.chrome.find_element(*self.BUTTON).click()
            login_confirmation = self.chrome.find_element(*self.SUCCESS).text
            if login_confirmation == "Secure Area":
                P_found = True
                print(f'The secret password is: {word}')
                break
        assert P_found == True, "The password could not be hacked"






