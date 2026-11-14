    # language: pt
Funcionalidade: Listagem, Filtragem e Exclusão de Chamados

  Cenário: Filtrar chamados por status ordenando prioridade Alta no topo
    Dado que o sistema de chamados foi iniciado
    E existe um chamado com título "Trocar mouse", status "Aberto" 
    E prioridade "Baixa"
    E existe um chamado com título "Servidor fora do ar", status "Aberto" 
    E prioridade "Alta"
    E existe um chamado com título "Erro antigo", status "Fechado" 
    E prioridade "Alta"
    Quando filtrar os chamados pelo status "Aberto"
    Então o sistema deve retornar 2 chamados
    E o primeiro chamado da lista deve ter título "Servidor fora do ar" 
    E prioridade "Alta"

  Cenário: Filtrar chamados por prioridade
    Dado que o sistema de chamados foi iniciado
    E existe um chamado com título "Trocar mouse", status "Aberto" 
    E prioridade "Baixa"
    E existe um chamado com título "Dúvida no sistema", status "Aberto" 
    E prioridade "Media"
    Quando filtrar os chamados pela prioridade "Media"
    Então o sistema deve retornar 1 chamado
    E o primeiro chamado da lista deve ter título "Dúvida no sistema" 
    E prioridade "Media"

  Cenário: Excluir um chamado com status Aberto
    Dado que existe um chamado aberto com título "Monitor sem sinal" 
    E prioridade "Media"
    Quando excluir o chamado de ID 1
    Então o chamado de ID 1 não deve mais existir no sistema

  Cenário: Impedir exclusão de chamado que não está Aberto
    Dado que existe um chamado com título "Falha na rede", status "Em Andamento" 
    E prioridade "Alta"
    Quando tentar excluir o chamado de ID 1
    Então o sistema deve bloquear a ação com erro de validação

  Cenário: Impedir exclusão de chamado inexistente
    Dado que o sistema de chamados foi iniciado
    Quando tentar excluir o chamado de ID 999
    Então o sistema deve bloquear a ação com erro de validação