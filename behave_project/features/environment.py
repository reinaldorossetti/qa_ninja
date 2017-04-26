from helpers.page_base import PageBase
from helpers.browser import set_browser


def before_all(context):
    userdata = context.config.userdata
    context.browser = userdata.get("browser")
    context.url = userdata.get("url")
    context.login = userdata.get("login")
    context.password = userdata.get("password")
    context.driver = set_browser(context.browser)
    context.base = PageBase(context.driver)
