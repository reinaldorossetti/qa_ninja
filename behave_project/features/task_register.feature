# -*- coding: utf-8 -*-
@task_register
Feature: Task Register.

    Scenario: Task.
    Given A pagina de Projeto.
    When Selecionar o menu projeto "Teste - Criação Automatizada de Tarefas".
    And Em acoes selecione a opcao tarefa.
    And Preencher os campos na aba geral.
    | Tarefa                             | DataInicial | DataFinal | HorasPlanejadas |
    | CT 01 - Consultar dados cadastrais | 17/04/2017   | 20/04/2017 | 0,60          |
    And Preencher os campos na aba atribuicoes.
    | Recurso                   |
    | Jessica Santos de Paula   |
    And Salvar os dados da aba atribuicoes.
    And Salvar os dados da aba geral.
    Then Validar se os dados foram inseridos com sucesso.
    | Recurso                   | DataInicial |
    | Jessica Santos de Paula   | 17/04/2017  |