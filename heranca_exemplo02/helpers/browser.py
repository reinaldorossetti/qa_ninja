from selenium import webdriver


def SetBrowser(browser):
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
