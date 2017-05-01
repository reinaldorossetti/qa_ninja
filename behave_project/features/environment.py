# from helpers.page_base import PageBase
from helpers.browser import set_browser
from time import sleep


def before_all(context):

    userdata = context.config.userdata
    context.browser = userdata.get("browser")
    context.driver = set_browser(context.browser)

def after_all(context):
    context.thread.join()
    context.driver.quit()


    # No selenium jogo minha base para o context.base.
    #context.base = PageBase(context.driver)
