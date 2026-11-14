from behave import given, when, then
from src.service import ChamadoService


@given("que o sistema possui chamados cadastrados")
def step_sistema_com_chamados(context):
    context.service = ChamadoService()
    context.chamado = None
    context.erro = None


@given('que existe um chamado com ID {chamado_id:d} e status "{status}"')
def step_criar_chamado_status(context, chamado_id, status):
    if not hasattr(context, "service"):
        context.service = ChamadoService()
    while context.service._proximo_id <= chamado_id:
        chamado = context.service.abrir_chamado(
            f"Chamado {context.service._proximo_id}", "Descrição", "Media"
        )
    chamado.status = status
    context.chamado = chamado
    context.erro = None


@given('que existe um chamado com ID {chamado_id:d}, status "Fechado", solução preenchida e data registrada')
def step_criar_chamado_fechado(context, chamado_id):
    if not hasattr(context, "service"):
        context.service = ChamadoService()
    while context.service._proximo_id <= chamado_id:
        chamado = context.service.abrir_chamado(
            f"Chamado {context.service._proximo_id}", "Descrição", "Media"
        )
    context.service.encerrar_chamado(chamado.id, "Solução aplicada anteriormente")
    context.chamado = chamado
    context.erro = None


@when('eu solicito o encerramento do chamado {chamado_id:d} com a solução "{solucao}"')
def step_solicitar_encerramento(context, chamado_id, solucao):
    try:
        context.chamado = context.service.encerrar_chamado(chamado_id, solucao)
        context.erro = None
    except ValueError as e:
        context.erro = str(e)


@when("eu solicito o encerramento do chamado {chamado_id:d} sem informar a solução")
def step_solicitar_encerramento_sem_solucao(context, chamado_id):
    try:
        context.chamado = context.service.encerrar_chamado(chamado_id, "")
        context.erro = None
    except ValueError as e:
        context.erro = str(e)


@when("eu solicito a reabertura do chamado {chamado_id:d}")
def step_solicitar_reabertura(context, chamado_id):
    try:
        context.chamado = context.service.reabrir_chamado(chamado_id)
        context.erro = None
    except ValueError as e:
        context.erro = str(e)


@when("eu tento reabrir o chamado {chamado_id:d}")
def step_tentar_reabrir(context, chamado_id):
    try:
        context.chamado = context.service.reabrir_chamado(chamado_id)
        context.erro = None
    except ValueError as e:
        context.erro = str(e)


@then('o status do chamado {chamado_id:d} deve mudar para "{status_esperado}"')
def step_verificar_status_chamado(context, chamado_id, status_esperado):
    chamado = context.service.buscar_chamado(chamado_id)
    assert chamado.status == status_esperado


@then('o status do chamado {chamado_id:d} deve mudar para "Em Andamento" ou "Aberto"')
def step_verificar_status_reaberto(context, chamado_id):
    chamado = context.service.buscar_chamado(chamado_id)
    assert chamado.status in ("Em Andamento", "Aberto")


@then("a data de encerramento deve ser registrada com sucesso")
def step_verificar_data_registrada(context):
    assert context.chamado.data_encerramento is not None


@then("a solução aplicada deve ser salva corretamente")
def step_verificar_solucao_salva(context):
    assert context.chamado.solucao is not None and len(context.chamado.solucao) > 0


@then("a solução aplicada anterior deve ser limpa (vazia)")
def step_verificar_solucao_limpa(context):
    assert context.chamado.solucao is None


@then("a data anterior deve ser removida ou limpa")
def step_verificar_data_limpa(context):
    assert context.chamado.data_encerramento is None


@then("o sistema deve retornar um erro informando que apenas chamados fechados podem ser reabertos")
def step_verificar_erro_reabertura(context):
    assert context.erro is not None
    assert "apenas chamados fechados" in context.erro.lower()


@then('o sistema deve retornar um erro contendo "{trecho}"')
def step_verificar_erro_contendo(context, trecho):
    assert context.erro is not None
    assert trecho.lower() in context.erro.lower()
