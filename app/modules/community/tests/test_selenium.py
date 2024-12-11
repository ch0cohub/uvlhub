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
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver
from selenium.common.exceptions import TimeoutException, UnexpectedAlertPresentException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class TestTestcrearcomunidad():
  def setup_method(self, method):
    self.driver = initialize_driver()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  

  def test_testunirseaunacomunidad(self):
    host = get_host_for_selenium_testing()
    self.driver.get(f"{host}")
    self.driver.set_window_size(1850, 1053)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("user1@example.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-item:nth-child(5) .align-middle:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Create Community").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Nueva comunidad")
    self.driver.find_element(By.ID, "description").send_keys("Test unirse a comunidad")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".text-dark").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-item:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("user2@example.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.LINK_TEXT, "Communities").click()
    # Espera explícita de hasta 10 segundos para que el botón esté visible
    button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.btn-sm"))
    )
    button.click()

  
  
  
  def test_testcrearcomunidad(self):
    host = get_host_for_selenium_testing()
    self.driver.get(f"{host}")
    self.driver.set_window_size(1850, 1053)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("user1@example.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.LINK_TEXT, "Communities").click()
    self.driver.find_element(By.LINK_TEXT, "Create Community").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Crear una comunidad test")
    self.driver.find_element(By.ID, "description").click()
    self.driver.find_element(By.ID, "description").send_keys("comunidad nueva")
    self.driver.find_element(By.ID, "submit").click()
  
  
  def test_testvisitarunacomunidad(self):
    host = get_host_for_selenium_testing()
    self.driver.get(f"{host}")   
    self.driver.set_window_size(1850, 1053)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("user1@example.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-item:nth-child(5) .align-middle:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Create Community").click()
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Comunidad a visitar")
    self.driver.find_element(By.ID, "description").click()
    self.driver.find_element(By.ID, "description").send_keys("Comunidad a visitar")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".text-dark").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-item:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("user2@example.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-item:nth-child(5) .align-middle:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".card-title").click()
  
  
  def test_actualizarunacomunidad(self):
    host = get_host_for_selenium_testing()
    self.driver.get(f"{host}")   
    self.driver.set_window_size(1850, 1053)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("user1@example.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-item:nth-child(5) .align-middle:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-warning").click()
    self.driver.find_element(By.ID, "description").click()
    self.driver.find_element(By.ID, "description").send_keys("Una comunidad de ciencias sin más ACTUALIZADO")
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("Comunidad de ciencias ACTUALIZADO")
    self.driver.find_element(By.ID, "submit").click()
  
  



  def test_eliminarcomunidad(self):
    host = get_host_for_selenium_testing()
    self.driver.get(f"{host}")  
    self.driver.set_window_size(1850, 1053)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    self.driver.find_element(By.ID, "email").click()
    self.driver.find_element(By.ID, "email").send_keys("user1@example.com")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("1234")
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-item:nth-child(5) .align-middle:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(1) form:nth-child(1) > .btn").click()
  


  
  
