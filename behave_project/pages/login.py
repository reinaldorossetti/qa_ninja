"""
Author: Reinaldo Mateus R J, Test version: 0.2
"""
from helpers.page_base import PageBase

class LoginTest(PageBase):

    login_page = {
        'login':'id=tl_login',
        'password':'id=tl_password',
        'submit':'css selector=input[type=\'submit\']',
        'title':'div.menu_title span'
    }

    def test_login_password_ok(self, tl_login, tl_password, user_type):

        self.user_type = user_type
        elem_login = self.wait_(self.login_page['login'])
        elem_login.send_keys(tl_login)
        elem_password = self.wait_(self.login_page['password'])
        elem_password.send_keys(tl_password)
        elem_button = self.wait_(self.login_page['submit'])
        elem_button.submit()

        return True

    def validar_login(self):

        self.driver.switch_to.frame("titlebar")
        confirm = self.wait_(self.login_page['title'])

        print(confirm.text)
        if self.user_type in confirm.text:
            return "Passed"
        else:
            return "Fail"
