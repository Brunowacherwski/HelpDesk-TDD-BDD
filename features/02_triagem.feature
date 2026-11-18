# language: pt
Funcionalidade: Triagem e Priorização de Chamados

  Cenário: Cadastrar uma nova prioridade válida
    Dado que o sistema de chamados foi iniciado
    Quando cadastrar a nova prioridade "Critica"
    Então a prioridade "Critica" deve estar na lista de prioridades do sistema

  Cenário: Impedir cadastro de prioridade vazia
    Dado que o sistema de chamados foi iniciado
    Quando tentar cadastrar a prioridade vazia ""
    Então o sistema deve bloquear a ação com a mensagem "O nome da prioridade é obrigatório."

  Cenário: Impedir cadastro de prioridade duplicada
    Dado que o sistema de chamados foi iniciado
    Quando tentar cadastrar a prioridade duplicada "Alta"
    Então o sistema deve bloquear a ação com a mensagem "Prioridade já cadastrada."

  Cenário: Atribuir técnico a um chamado aberto
    Dado que existe um chamado aberto com título "Impressora sem conexão"
    E o chamado possuir prioridade "Media"
    Quando atribuir o técnico "Carlos" ao chamado de ID 1
    Então o chamado deve possuir o técnico "Carlos"
    E o status do chamado deve ser atualizado para "Em Andamento"

  Cenário: Impedir atribuição de técnico vazio
    Dado que existe um chamado aberto com título "Impressora sem conexão"
    Quando tentar atribuir o técnico vazio "" ao chamado de ID 1
    Então o sistema deve bloquear a ação com a mensagem "O nome do técnico é obrigatório."

  Cenário: Impedir atribuição de técnico em chamado fechado
    Dado que existe um chamado aberto com título "Mouse quebrado"
    E o chamado possuir prioridade "Baixa"
    E o chamado possuir status "Fechado"
    Quando tentar atribuir o técnico "Carlos" ao chamado de ID 1
    Então o sistema deve bloquear a ação com a mensagem "Chamado #1 já está fechado."

  Cenário: Alterar a prioridade de um chamado aberto
    Dado que existe um chamado aberto com título "Sistema lento"
    E o chamado possuir prioridade "Baixa"
    Quando alterar a prioridade do chamado de ID 1 para "Alta"
    Então a prioridade do chamado deve ser atualizada para "Alta"

  Cenário: Impedir alteração de prioridade em chamado fechado
    Dado que existe um chamado aberto com título "Teclado falhando"
    E o chamado possuir prioridade "Baixa"
    E o chamado possuir status "Fechado"
    Quando tentar alterar a prioridade do chamado de ID 1 para "Alta"
    Então o sistema deve bloquear a ação com a mensagem "Chamado #1 já está fechado."

  Cenário: Impedir alteração para prioridade inválida
    Dado que existe um chamado aberto com título "Sistema lento"
    Quando tentar alterar a prioridade do chamado de ID 1 para "Inexistente"
    Então o sistema deve bloquear a ação com a mensagem "Prioridade inválida."