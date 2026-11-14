# language: pt
Funcionalidade: Gestão do Ciclo de Vida do Chamado (Encerramento e Reabertura)
  Como um técnico ou operador do sistema de help desk
  Quero encerrar chamados concluídos e reabrir chamados quando necessário
  Para manter o histórico e o status dos atendimentos atualizados

  Contexto:
    Dado que o sistema possui chamados cadastrados

  Cenário: Encerrar um chamado com sucesso
    Dado que existe um chamado com ID 1 e status "Em Andamento"
    Quando eu solicito o encerramento do chamado 1 com a solução "Reinicialização do serviço de rede"
    Então o status do chamado 1 deve mudar para "Fechado"
    E a data de encerramento deve ser registrada com sucesso
    E a solução aplicada deve ser salva corretamente

  Cenário: Reabrir um chamado fechado com sucesso
    Dado que existe um chamado com ID 1, status "Fechado", solução preenchida e data registrada
    Quando eu solicito a reabertura do chamado 1
    Então o status do chamado 1 deve mudar para "Em Andamento"
    E a solução aplicada anterior deve ser limpa (vazia)
    E a data anterior deve ser removida ou limpa

  Cenário: Tentativa de reabrir um chamado que não está fechado
    Dado que existe um chamado com ID 2 e status "Aberto"
    Quando eu tento reabrir o chamado 2
    Então o sistema deve retornar um erro informando que apenas chamados fechados podem ser reabertos