"""
Author: Reinaldo Mateus R J, Test version: 0.1
Leia: https://docs.python.org/3.6/tutorial/classes.html#multiple-inheritance
"""

import pages.login
import pages.logout
import pages.find_test_case
from helpers.browser import SetBrowser

class testsCase(pages.login.LoginTest, pages.logout.LogoutTest, pages.find_test_case.FindTestCase):


    def __init__(self):
        self.base_url = "http://192.168.236.130/"
        driver = SetBrowser("chrome")
        super(testsCase, self).__init__(driver)

    def test01(self):

        # login test.
        self.driver.get(self.base_url + "login.php")
        self.test_login_password_ok("user", "bitnami", "admin")
        print(self.validar_login())

        # find testcase.
        self.find("TC-1")
        self.result_find("TC-1")

        # logout test.
        self.logout_test()
        print(self.validar_logout())

        # sair do browser.
        self.driver.quit()


if __name__ == '__main__':
    test = testsCase()
    test.test01()
