from selenium import webdriver


def set_browser(browser):

    browser = browser.lower()
    if browser == "firefox":

        driver = webdriver.Firefox()
        return driver

    elif browser == "chrome":
        driver = webdriver.Chrome()
        return driver

    elif browser == "ie":
        driver = webdriver.Ie()
        return driver

