# language: pt
Funcionalidade: Abertura e Consulta de Chamados

  Cenário: Abrir um chamado com dados válidos
    Dado que o sistema de chamados foi iniciado
    Quando abrir um chamado com título "Erro no sistema" 
    E chamado possuir prioridade "Alta"
    Então o chamado deve ser criado com status "Aberto" 
    E o chamado possuir ID 1

  Cenário: Impedir abertura de chamado sem título
    Dado que o sistema de chamados foi iniciado
    Quando tentar abrir um chamado sem título
    Então o sistema deve bloquear a ação com erro de validação

  Cenário: Buscar um chamado existente pelo ID
    Dado que existe um chamado aberto com título "Monitor sem sinal" 
    E o chamado possuir prioridade "Media"
    Quando buscar o chamado de ID 1
    Então o sistema deve retornar o chamado com título "Monitor sem sinal"