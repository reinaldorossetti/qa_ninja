"""
Author: Reinaldo Mateus R J, Test version: 0.2
"""
from helpers.page_base import PageBase


class FindTestCase(PageBase):

    find_menu = {
        'search_input':'css selector=form#searchTC input[name=\'targetTestCase\']',
        'search_img':'css selector=form#searchTC img[onclick*=\'searchTC\']',
        'search_result':'css selector=.workBack h2'
    }

    def find(self, index):

        # Procura o elemento na tela via CSS Selector.
        elem_input_text = self.wait_(self.find_menu['search_input'])
        elem_input_text.clear() # limpa o campo.
        elem_input_text.send_keys(index) # envia o valor para o campo.
        elem_search = self.wait_(self.find_menu['search_img'])
        elem_search.click()

        return True

    def result_find(self, index):

        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('mainframe')

        # Procura o elemento na tela via CSS Selector.
        elem_img_find = self.wait_(self.find_menu['search_result'])
        print(elem_img_find.text)

        if index in elem_img_find.text:
            return "Passed"
        else:
            return "Fail"
