# -*- coding: utf-8 -*-
@logout
Feature: Logout

  Scenario: Cenario Logout.
    Given Esteja na pagina ativa.
    When Efetuar o logout no sistema.
    Then Verificar se o logout foi efetuado com sucesso.
