"""
Author: Reinaldo Mateus R J, Test version: 0.2
"""
from helpers.page_base import PageBase

class LogoutTest(PageBase):

    logout_page = {
        'img':'css selector=img[title*=\'Logout\']',
    }

    def logout_test(self):

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame("titlebar")

        # Procura o elemento na tela via CSS Selector.
        elem_logout = self.wait_(self.logout_page['img'])
        # Envia o click para o botao.
        elem_logout.click()

    def validar_logout(self):

        elem_logout = self.wait_not(self.logout_page['img'])
        print(elem_logout)

        if elem_logout:
            return "Passed"
        else:
            return "Fail"