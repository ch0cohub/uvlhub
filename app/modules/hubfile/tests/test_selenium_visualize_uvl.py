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


class TestA:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_a(self):
        self.driver.get("http://localhost:5000/")
        self.driver.set_window_size(1050, 715)
        self.driver.find_element(By.LINK_TEXT, "Sample dataset 4").click()
        element = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.ID, "btnGroupDropExport10"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        element.click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "Glencoe").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, "fileViewerModalLabel"), "Feature model view"
            )
        )
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-close").click()
        element = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.ID, "btnGroupDropExport11"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        element.click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "DIMACS").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, "fileViewerModalLabel"), "Feature model view"
            )
        )
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".btn-close").click()
        element = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.ID, "btnGroupDropExport12"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(1)
        element.click()
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, "SPLOT").click()
        WebDriverWait(self.driver, 30).until(
            expected_conditions.text_to_be_present_in_element(
                (By.ID, "fileViewerModalLabel"), "Feature model view"
            )
        )
        self.driver.find_element(By.CSS_SELECTOR, ".btn-close").click()
