"""
Author: Reinaldo Mateus R J, Test version: 0.1
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class FindTestCase:

    def find(self, driver, index):

        wait = WebDriverWait(driver, 60)

        # Procura o elemento na tela via CSS Selector.
        elem_input_text = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                                    "form#searchTC input[name='targetTestCase']"))
        elem_input_text.clear() # limpa o campo.
        elem_input_text.send_keys(index) # envia o valor para o campo.

        elem_search = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                                    "form#searchTC img[onclick*='searchTC']"))
        elem_search.click()

        return True

    def result_find(self, driver, index):

        wait = WebDriverWait(driver, 60)
        driver.switch_to.parent_frame()
        driver.switch_to.frame('mainframe')

        # Procura o elemento na tela via CSS Selector.
        elem_img_find = wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR,
                                                                    ".workBack h2"))
        print(elem_img_find.text)

        if index in elem_img_find.text:
            return "Passed"
        else:
            return "Fail"
