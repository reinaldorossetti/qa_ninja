from behave import given, when, then, step
from pages.page_login import PageLogin
from pages.principal_page import PrincipalPage


@given(u'A pagina de login.')
def step_impl(context):
    context.base.open(context.url)
    context.PageLogin = PageLogin(context.driver)
    context.PrincipalPage = PrincipalPage(context.driver)


@when(u'Digitar o login.')
def step_impl(context):
   valida = context.PageLogin.login()
   if valida == True:
      print ("passou, login")
   else:
      print ("nao passou, login")

@when(u'Digitar o password.')
def step_impl(context):
    print (context.password)
    valida = context.PageLogin.password()
    if valida == True:
        print("passou, password")
    else:
        print("nao passou, password")


@when(u'Efetuar a autenticacao.')
def step_impl(context):
    context.PageLogin.submit_test()


@then(u'Verificar se a autenticacao foi realizado com sucesso.')
def step_impl(context):
    valida = context.PageLogin.check_out()
    if valida == True:
        print("Passou com sucesso!")
    else:
        print("Nao passou!")
