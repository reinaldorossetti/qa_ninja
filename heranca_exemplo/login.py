"""
Author: Reinaldo Mateus R J, Test version: 0.1
"""

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class LoginTest:

    def __init__(self):

        self.user_type = ""
        self.wait = ""

    def test_login_password_ok(self, tl_login, tl_password, user_type, driver):

        self.user_type = user_type
        self.wait = WebDriverWait(driver, 60)

        elem_login = self.wait.until(lambda driver:
                                     driver.find_element_by_id("tl_login"))
        elem_login.send_keys(tl_login)
        elem_password = self.wait.until(lambda driver:
                                        driver.find_element_by_id("tl_password"))
        elem_password.send_keys(tl_password)
        elem_button = self.wait.until(lambda driver:
                                      driver.find_element_by_css_selector("input[type='submit']"))
        elem_button.send_keys(Keys.ENTER)

        return True

    def validar_login(self, driver):

        self.wait = WebDriverWait(driver, 60)
        driver.switch_to.frame("titlebar")
        confirm = self.wait.until(lambda driver: driver.find_element_by_css_selector("div.menu_title span"))

        print(confirm.text)
        if self.user_type in confirm.text:
            return "Passed"
        else:
            return "Fail"
