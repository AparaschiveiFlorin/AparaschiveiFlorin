# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestZtoAName():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_ztoAName(self):
    # Test name: ZtoAName
    # Step # | name | target | value
    # 1 | open | /en/ | 
    self.driver.get("http://34.118.122.203/en/")
    # 2 | setWindowSize | 945x1020 | 
    self.driver.set_window_size(945, 1020)
    # 3 | click | css=a > .hidden-sm-down | 
    self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
    # 4 | click | id=field-email | 
    self.driver.find_element(By.ID, "field-email").click()
    # 5 | type | id=field-email | alexandruflorin1989@gmail.com
    self.driver.find_element(By.ID, "field-email").send_keys("alexandruflorin1989@gmail.com")
    # 6 | type | id=field-password | Floalex
    self.driver.find_element(By.ID, "field-password").send_keys("Floalex")
    # 7 | click | id=submit-login | 
    self.driver.find_element(By.ID, "submit-login").click()
    # 8 | click | css=.logo | 
    self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
    # 9 | click | linkText=All new products | 
    self.driver.find_element(By.LINK_TEXT, "All new products").click()
    # 10 | click | css=.select-title | 
    self.driver.find_element(By.CSS_SELECTOR, ".select-title").click()
    # 11 | click | linkText=Name, Z to A | 
    self.driver.find_element(By.LINK_TEXT, "Name, Z to A").click()
    # 12 | click | css=.js-product:nth-child(1) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
    # 13 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 14 | click | css=.cart-content-btn > .btn-primary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
    # 15 | click | css=.text-sm-center > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
    # 16 | click | linkText=add new address | 
    self.driver.find_element(By.LINK_TEXT, "add new address").click()
    # 17 | click | id=field-address1 | 
    self.driver.find_element(By.ID, "field-address1").click()
    # 18 | type | id=field-address1 | Emil Racovita
    self.driver.find_element(By.ID, "field-address1").send_keys("Emil Racovita")
    # 19 | click | id=field-city | 
    self.driver.find_element(By.ID, "field-city").click()
    # 20 | type | id=field-city | Brasov
    self.driver.find_element(By.ID, "field-city").send_keys("Brasov")
    # 21 | click | id=field-id_state | 
    self.driver.find_element(By.ID, "field-id_state").click()
    # 22 | select | id=field-id_state | label=AA
    dropdown = self.driver.find_element(By.ID, "field-id_state")
    dropdown.find_element(By.XPATH, "//option[. = 'AA']").click()
    # 23 | click | id=field-postcode | 
    self.driver.find_element(By.ID, "field-postcode").click()
    # 24 | type | id=field-postcode | 50011
    self.driver.find_element(By.ID, "field-postcode").send_keys("50011")
    # 25 | click | name=confirm-addresses | 
    self.driver.find_element(By.NAME, "confirm-addresses").click()
    # 26 | click | name=confirmDeliveryOption | 
    self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
    # 27 | click | id=payment-option-3 | 
    self.driver.find_element(By.ID, "payment-option-3").click()
    # 28 | click | id=conditions_to_approve[terms-and-conditions] | 
    self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
    # 29 | click | css=.ps-shown-by-js > .btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()
  
