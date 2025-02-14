"""
Author: Reinaldo Mateus R J, Test version: 0.1
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class LogoutTest:

    def logout_test(self, driver):

        self.driver = driver
        wait = WebDriverWait(self.driver, 60)
        driver.switch_to.default_content()
        driver.switch_to.frame("titlebar")

        # Procura o elemento na tela via CSS Selector.
        elem_logout = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, "img[title*='Logout']"))
        # Envia o click para o botao.
        elem_logout.click()

    def validar_logout(self, driver):

        wait = WebDriverWait(self.driver, 60)
        elem_logout = wait.until_not(lambda driver: driver.find_element(By.CSS_SELECTOR, "img[title*='Logout']"))
        print(elem_logout)

        if elem_logout:
            return "Passed"
        else:
            return "Fail"