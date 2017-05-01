from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

class PageBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def wait_(self, locator):
        locator = locator.split("=", 1)
        element = self.wait.until(visibility_of_element_located(locator))
        return element

    def wait_not(self, locator):
        locator = locator.split("=", 1)
        element = self.wait.until_not(visibility_of_element_located(locator))
        return element