import pytest
from behave import given, when, then
from src.service import ChamadoService


# bruno

@given("que o sistema de chamados foi iniciado")
def step_iniciar_sistema(context):
    context.service = ChamadoService()
    context.chamado = None
    context.erro = None


@given('que existe um chamado aberto com título "{titulo}"')
def step_criar_chamado_aberto(context, titulo):
    context.service = ChamadoService()
    context.chamado = context.service.abrir_chamado(titulo, "Descrição padrão", "Media")
    context.erro = None


@given('o chamado possuir prioridade "{prioridade}"')
def step_definir_prioridade_dado(context, prioridade):
    context.chamado.prioridade = prioridade


@when('abrir um chamado com título "{titulo}"')
def step_abrir_chamado(context, titulo):
    context.chamado = context.service.abrir_chamado(titulo, "Descrição", "Media")


@when('chamado possuir prioridade "{prioridade}"')
def step_definir_prioridade_quando(context, prioridade):
    context.chamado.prioridade = prioridade


@when("tentar abrir um chamado sem título")
def step_abrir_sem_titulo(context):
    try:
        context.service.abrir_chamado("", "Descrição")
    except ValueError as e:
        context.erro = str(e)


@when("buscar o chamado de ID {chamado_id:d}")
def step_buscar_chamado(context, chamado_id):
    context.chamado = context.service.buscar_chamado(chamado_id)


@then('o chamado deve ser criado com status "{status}"')
def step_verificar_status_criacao(context, status):
    assert context.chamado.status == status


@then("o chamado possuir ID {chamado_id:d}")
def step_verificar_id_criacao(context, chamado_id):
    assert context.chamado.id == chamado_id


@then('o sistema deve retornar o chamado com título "{titulo_esperado}"')
def step_verificar_titulo(context, titulo_esperado):
    assert context.chamado.titulo == titulo_esperado


@then("o sistema deve bloquear a ação com erro de validação")
def step_verificar_erro(context):
    assert context.erro is not None


# lucas

@given('existe um chamado com título "{titulo}"')
@given('que existe um chamado com título "{titulo}"')
def step_criar_chamado_apenas_titulo(context, titulo):
    if not hasattr(context, "service") or context.service is None:
        context.service = ChamadoService()
        context.erro = None
    context.chamado = context.service.abrir_chamado(titulo, "Descrição padrão", "Media")


@when('filtrar os chamados pelo status "{status}"')
def step_filtrar_por_status(context, status):
    context.resultados = context.service.filtrar_chamados(status=status)


@when('filtrar os chamados pela prioridade "{prioridade}"')
def step_filtrar_por_prioridade(context, prioridade):
    context.resultados = context.service.filtrar_chamados(prioridade=prioridade)


@when("excluir o chamado de ID {chamado_id:d}")
def step_excluir_chamado(context, chamado_id):
    context.service.excluir_chamado(chamado_id)


@when("tentar excluir o chamado de ID {chamado_id:d}")
def step_tentar_excluir_chamado(context, chamado_id):
    try:
        context.service.excluir_chamado(chamado_id)
    except ValueError as e:
        context.erro = str(e)


@then("o sistema deve retornar {quantidade:d} chamado")
@then("o sistema deve retornar {quantidade:d} chamados")
def step_verificar_quantidade_chamados(context, quantidade):
    assert len(context.resultados) == quantidade


@then('o primeiro chamado da lista deve ter título "{titulo}"')
def step_verificar_titulo_primeiro_da_lista(context, titulo):
    assert len(context.resultados) > 0
    assert context.resultados[0].titulo == titulo


@then('o primeiro chamado da lista deve ter prioridade "{prioridade}"')
def step_verificar_prioridade_primeiro_da_lista(context, prioridade):
    assert len(context.resultados) > 0
    assert context.resultados[0].prioridade == prioridade


@then("o chamado de ID {chamado_id:d} não deve mais existir no sistema")
def step_verificar_chamado_excluido(context, chamado_id):
    with pytest.raises(ValueError, match="não encontrado"):
        context.service.buscar_chamado(chamado_id)

@given('o chamado possuir status "{status}"')
def step_definir_status_dado(context, status):
    context.chamado.status = status


@then('o sistema deve bloquear a ação com a mensagem "{mensagem}"')
def step_verificar_mensagem_exata(context, mensagem):
    assert context.erro == mensagem        