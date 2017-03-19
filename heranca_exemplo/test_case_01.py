"""
Author: Reinaldo Mateus R J, Test version: 0.1
"""

from selenium import webdriver
import login
import logout
import find_test_case

class testsCase(login.LoginTest, logout.LogoutTest, find_test_case.FindTestCase):


    def __init__(self):
        self.base_url = "http://192.168.236.128/"
        self.driver = webdriver.Chrome()

    def test01(self):

        # login test.
        self.driver.get(self.base_url + "login.php")
        self.test_login_password_ok("user", "bitnami", "admin", self.driver)
        print(self.validar_login(self.driver))

        # find testcase.
        self.find(self.driver, "TC-1")
        self.result_find(self.driver, "TC-1")

        # logout test.
        self.logout_test(self.driver)
        print(self.validar_logout(self.driver))


if __name__ == '__main__':
    test = testsCase()
    test.test01()
