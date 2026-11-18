# language: pt
Funcionalidade: Listagem e Exclusão de Chamados

  Cenário: Filtrar chamados por status ordenando prioridade Alta no topo
    Dado que o sistema de chamados foi iniciado
    E existe um chamado com título "Trocar mouse"
    E o chamado possuir status "Aberto"
    E o chamado possuir prioridade "Baixa"
    E existe um chamado com título "Servidor fora do ar"
    E o chamado possuir status "Aberto"
    E o chamado possuir prioridade "Alta"
    E existe um chamado com título "Erro antigo"
    E o chamado possuir status "Fechado"
    E o chamado possuir prioridade "Alta"
    Quando filtrar os chamados pelo status "Aberto"
    Então o sistema deve retornar 2 chamados
    E o primeiro chamado da lista deve ter título "Servidor fora do ar"
    E o primeiro chamado da lista deve ter prioridade "Alta"

  Cenário: Filtrar chamados por prioridade
    Dado que o sistema de chamados foi iniciado
    E existe um chamado com título "Trocar mouse"
    E o chamado possuir status "Aberto"
    E o chamado possuir prioridade "Baixa"
    E existe um chamado com título "Dúvida no sistema"
    E o chamado possuir status "Aberto"
    E o chamado possuir prioridade "Media"
    Quando filtrar os chamados pela prioridade "Media"
    Então o sistema deve retornar 1 chamado
    E o primeiro chamado da lista deve ter título "Dúvida no sistema"
    E o primeiro chamado da lista deve ter prioridade "Media"

  Cenário: Excluir um chamado com status Aberto
    Dado que o sistema de chamados foi iniciado
    E existe um chamado com título "Monitor sem sinal"
    E o chamado possuir status "Aberto"
    E o chamado possuir prioridade "Media"
    Quando excluir o chamado de ID 1
    Então o chamado de ID 1 não deve mais existir no sistema

  Cenário: Impedir exclusão de chamado que não está Aberto
    Dado que o sistema de chamados foi iniciado
    E existe um chamado com título "Falha na rede"
    E o chamado possuir status "Em Andamento"
    E o chamado possuir prioridade "Alta"
    Quando tentar excluir o chamado de ID 1
    Então o sistema deve bloquear a ação com a mensagem "O chamado #1 possui status 'Em Andamento'. Apenas chamados 'Abertos' podem ser excluídos."

  Cenário: Impedir exclusão de chamado inexistente
    Dado que o sistema de chamados foi iniciado
    Quando tentar excluir o chamado de ID 999
    Então o sistema deve bloquear a ação com a mensagem "Chamado 999 não encontrado."