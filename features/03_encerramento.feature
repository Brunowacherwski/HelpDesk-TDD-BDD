# language: pt
Funcionalidade: Encerramento e Reabertura de Chamados

  Cenário: Encerrar um chamado aberto informando solução e data atual do sistema
    Dado que o sistema de chamados foi iniciado na data atual "17/11/2026"
    E que existe um chamado aberto com título "Falha no servidor de e-mail"
    E o chamado possuir prioridade "Alta"
    Quando encerrar o chamado de ID 1 com a solução "Serviço SMTP reiniciado" na data "17/11/2026"
    Então o status do chamado deve ser atualizado para "Fechado"
    E a solução registrada no chamado deve ser "Serviço SMTP reiniciado"
    E a data de encerramento do chamado deve ser "17/11/2026"

  Cenário: Impedir encerramento de chamado sem informar solução
    Dado que o sistema de chamados foi iniciado na data atual "17/11/2026"
    E que existe um chamado aberto com título "Falha no servidor de e-mail"
    Quando tentar encerrar o chamado de ID 1 com a solução "" na data "17/11/2026"
    Então o sistema deve bloquear a ação com a mensagem "A solução do chamado é obrigatória."
    E o status do chamado deve permanecer "Aberto"

  Cenário: Impedir encerramento de chamado que já está fechado
    Dado que o sistema de chamados foi iniciado na data atual "17/11/2026"
    E que existe um chamado aberto com título "Troca de monitor"
    E o chamado de ID 1 foi encerrado com a solução "Monitor trocado" na data "17/11/2026"
    Quando tentar encerrar o chamado de ID 1 com a solução "Nova troca" na data "17/11/2026"
    Então o sistema deve bloquear a ação com a mensagem "Chamado #1 já está fechado."

  Cenário: Reabrir um chamado fechado com sucesso
    Dado que o sistema de chamados foi iniciado na data atual "17/11/2026"
    E que existe um chamado aberto com título "Queda de rede no 2º andar"
    E o chamado de ID 1 foi encerrado com a solução "Switch reiniciado" na data "17/11/2026"
    Quando reabrir o chamado de ID 1
    Então o status do chamado deve ser atualizado para "Aberto"
    E o chamado não deve possuir solução registrada
    E o chamado não deve possuir data de encerramento

  Cenário: Impedir reabertura de chamado que já está aberto
    Dado que o sistema de chamados foi iniciado na data atual "17/11/2026"
    E que existe um chamado aberto com título "Queda de rede no 2º andar"
    Quando tentar reabrir o chamado de ID 1
    Então o sistema deve bloquear a ação com a mensagem "Apenas chamados fechados podem ser reabertos."