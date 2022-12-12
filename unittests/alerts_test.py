import unittest

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By
class Alerts(unittest.TestCase):
	JS_ALERT_BUTTON = (By.XPATH,'//*[text()="Click for JS Alert"]')
	JS_CONFIRM_BUTTON = (By.XPATH,"//*[text()='Click for JS Confirm']")
	JS_PROMPT_BUTTON = (By.XPATH,"//*[text()='Click for JS Prompt']")
	ALERT_ACTION_MESSAGE = (By.ID,"result")

	def setUp(self) -> None:
		self.chrome = webdriver.Chrome()
		self.chrome.maximize_window()
		self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
		self.chrome.implicitly_wait(2)

	def tearDown(self) -> None:
		self.chrome.quit()

	@unittest.skip
	def test_js_alert_accept(self):
		self.chrome.find_element(*self.JS_ALERT_BUTTON).click()
		js_alert = self.chrome.switch_to.alert
		js_alert.accept()
		js_alert_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
		expected_text = 'You successfully clicked an alert'
		assert js_alert_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_alert_text}"

	@unittest.skip
	def test_js_confirm_accept(self):
		self.chrome.find_element(*self.JS_CONFIRM_BUTTON).click()
		js_confirm = self.chrome.switch_to.alert
		js_confirm.accept()
		js_confirm_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
		expected_text = 'You clicked: Ok'
		assert js_confirm_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_confirm_text}"

	@unittest.skip
	def test_js_confirm_cancel(self):
		self.chrome.find_element(*self.JS_CONFIRM_BUTTON).click()
		js_confirm = self.chrome.switch_to.alert
		js_confirm.dismiss()
		js_confirm_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
		expected_text = 'You clicked: Cancel'
		assert js_confirm_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_confirm_text}"

	def test_js_prompt_accept_no_text_insert(self):
		self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
		js_prompt = self.chrome.switch_to.alert
		js_prompt.accept()
		js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
		expected_text = 'You entered:'
		assert js_prompt_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_prompt_text}"

	def test_js_prompt_cancel_no_text_inserted(self):
		self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
		js_prompt = self.chrome.switch_to.alert
		js_prompt.dismiss()
		js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
		expected_text = 'You entered: null'
		assert js_prompt_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_prompt_text}"

	def test_js_prompt_accept_text_insert(self):
		self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
		js_prompt = self.chrome.switch_to.alert
		js_prompt.send_keys("test")
		js_prompt.accept()
		js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
		expected_text = 'You entered: test'
		assert js_prompt_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_prompt_text}"

	def test_js_prompt_cancel_text_inserted(self):
		self.chrome.find_element(*self.JS_PROMPT_BUTTON).click()
		js_prompt = self.chrome.switch_to.alert
		js_prompt.send_keys("test")
		js_prompt.dismiss()
		js_prompt_text = self.chrome.find_element(*self.ALERT_ACTION_MESSAGE).text
		expected_text = 'You entered: null'
		assert js_prompt_text == expected_text, f"ERROR: Expected: {expected_text}, Actual: {js_prompt_text}"
