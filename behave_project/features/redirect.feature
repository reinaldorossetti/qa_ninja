# -*- coding: utf-8 -*-

@redirect_url
Feature: Envenenamento de hosts.

  Scenario: Envenenamento do local host.
    Given A url de um determinado site.
        """
        http://www.caixa.gov.br
        """

    When Mudar para o site invalido.
    Then Validar se o antivirus realizou o redirecionamento da url falsa.
