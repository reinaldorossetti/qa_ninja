# -*- coding: utf-8 -*-

@envenenar_host
Feature: Envenenamento de hosts.

    Scenario: Envenenamento do local host.
    Given O arquivo de hosts do sistema.
    When Envenenar o hosts com uma ip falso.
        | IP        | SITE                       |
        | 127.0.0.1 | behave.readthedocs.io      |

        And Remover as permissoes de escrita do arquivo.
    Then Validar se o antivirus realizou o comentario da linha.
        | IP        | SITE                       |
        | 127.0.0.1 | behave.readthedocs.io      |
        And O arquivo hots deve ter permissao de escrita.