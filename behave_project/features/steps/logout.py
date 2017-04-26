from behave import given, when, then, step
from pages.page_login import PageLogin
from selenium.webdriver.common.alert import Alert

@given(u'Esteja na pagina ativa.')
def step_impl(context):

    context.PageLogin = PageLogin(context.driver)
    context.driver.switch_to_window(context.driver.window_handles[-1])   # altera o foco para a janela principal
    valida = context.base.wait_element(context.PageLogin.logout_page['botao_logout'], 20)
    if valida == True:
        print("passou, valida pagina")
    else:
        print("nao passou, valida pagina")

@when(u'Efetuar o logout no sistema.')
def step_impl(context):
    context.base.submit(context.PageLogin.logout_page['botao_logout'])
    Alert(context.driver).accept()


@then(u'Verificar se o logout foi efetuado com sucesso.')
def step_impl(context):
    valida = context.PageLogin.check_logout()
    if valida == True:
        print("passou, valida logout")
    else:
        print("nao passou, valida logout")
