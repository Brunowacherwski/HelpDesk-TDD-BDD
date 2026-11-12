from behave import given, when, then
from src.service import ChamadoService


@given("que o sistema de chamados foi iniciado")
def step_iniciar_sistema(context):
    context.service = ChamadoService()
    context.chamado = None
    context.erro = None


@given('que existe um chamado aberto com título "{titulo}" e prioridade "{prioridade}"')
def step_criar_chamado_aberto(context, titulo, prioridade):
    context.service = ChamadoService()
    context.chamado = context.service.abrir_chamado(titulo, "Descrição padrão", prioridade)
    context.erro = None


@when('abrir um chamado com título "{titulo}" e prioridade "{prioridade}"')
def step_abrir_chamado(context, titulo, prioridade):
    context.chamado = context.service.abrir_chamado(titulo, "Descrição", prioridade)


@when("tentar abrir um chamado sem título")
def step_abrir_sem_titulo(context):
    try:
        context.service.abrir_chamado("", "Descrição")
    except ValueError as e:
        context.erro = str(e)


@when("buscar o chamado de ID {chamado_id:d}")
def step_buscar_chamado(context, chamado_id):
    context.chamado = context.service.buscar_chamado(chamado_id)


@then('o chamado deve ser criado com status "{status}" e ID {chamado_id:d}')
def step_verificar_criacao(context, status, chamado_id):
    assert context.chamado.status == status
    assert context.chamado.id == chamado_id


@then('o sistema deve retornar o chamado com título "{titulo_esperado}"')
def step_verificar_titulo(context, titulo_esperado):
    assert context.chamado.titulo == titulo_esperado


@then("o sistema deve bloquear a ação com erro de validação")
def step_verificar_erro(context):
    assert context.erro is not None