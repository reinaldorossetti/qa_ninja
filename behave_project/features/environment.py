# from helpers.page_base import PageBase
from helpers.browser import set_browser
import threading
from time import sleep

def redirect(context):
    userdata = context.config.userdata
    url = userdata.get("url")
    if url == context.driver.current_url:
        context.driver.get("http://www.caixa.gov.net/")
        sleep(60)


def before_all(context):

    userdata = context.config.userdata
    context.browser = userdata.get("browser")
    context.driver = set_browser(context.browser)

    context.thread = threading.Thread(target=context.driver.redirect)
    context.thread.start()

def after_all(context):
    context.thread.join()
    context.driver.quit()


    # No selenium jogo minha base para o context.base.
    #context.base = PageBase(context.driver)
