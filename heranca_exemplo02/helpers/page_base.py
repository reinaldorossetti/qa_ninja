from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


class PageBase:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60)

    def wait_(self, locator):
        locator = locator.split("=", 1)
        self.wait.until(lambda driver: driver.find_element(locator[0], locator[1]))

    def wait_not(self, locator):
        locator = locator.split("=", 1)
        self.wait.until_not(lambda driver: driver.find_element(locator[0], locator[1]))