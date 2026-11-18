from datetime import datetime
from behave import given, when, then
from src.service import ChamadoService


@given('que o sistema de chamados foi iniciado na data atual "{data_str}"')
def step_iniciar_sistema_com_data(context, data_str):
    context.service = ChamadoService()
    context.data_atual = datetime.strptime(data_str, "%d/%m/%Y")
    context.chamado = None
    context.erro = None


@given('o chamado de ID {chamado_id:d} foi encerrado com a solução "{solucao}" na data "{data_str}"')
def step_chamado_ja_encerrado(context, chamado_id, solucao, data_str):
    data_enc = datetime.strptime(data_str, "%d/%m/%Y")
    context.chamado = context.service.encerrar_chamado(chamado_id, solucao, data_enc)


@when('encerrar o chamado de ID {chamado_id:d} com a solução "{solucao}" na data "{data_str}"')
def step_encerrar_chamado(context, chamado_id, solucao, data_str):
    data_enc = datetime.strptime(data_str, "%d/%m/%Y")
    context.chamado = context.service.encerrar_chamado(chamado_id, solucao, data_enc)


@when('tentar encerrar o chamado de ID {chamado_id:d} com a solução "{solucao}" na data "{data_str}"')
def step_tentar_encerrar_chamado(context, chamado_id, solucao, data_str):
    data_enc = datetime.strptime(data_str, "%d/%m/%Y")
    try:
        context.service.encerrar_chamado(chamado_id, solucao, data_enc)
    except ValueError as e:
        context.erro = str(e)


@when('tentar encerrar o chamado de ID {chamado_id:d} com a solução "" na data "{data_str}"')
def step_tentar_encerrar_chamado_sem_solucao(context, chamado_id, data_str):
    data_enc = datetime.strptime(data_str, "%d/%m/%Y")
    try:
        context.service.encerrar_chamado(chamado_id, "", data_enc)
    except ValueError as e:
        context.erro = str(e)


@when("reabrir o chamado de ID {chamado_id:d}")
def step_reabrir_chamado(context, chamado_id):
    context.chamado = context.service.reabrir_chamado(chamado_id)


@when("tentar reabrir o chamado de ID {chamado_id:d}")
def step_tentar_reabrir_chamado(context, chamado_id):
    try:
        context.service.reabrir_chamado(chamado_id)
    except ValueError as e:
        context.erro = str(e)


@then('a solução registrada no chamado deve ser "{solucao_esperada}"')
def step_verificar_solucao(context, solucao_esperada):
    assert context.chamado.solucao == solucao_esperada


@then('a data de encerramento do chamado deve ser "{data_str}"')
def step_verificar_data_encerramento(context, data_str):
    data_esperada = datetime.strptime(data_str, "%d/%m/%Y")
    assert context.chamado.data_encerramento == data_esperada


@then('o status do chamado deve permanecer "{status}"')
def step_verificar_status_permanece(context, status):
    assert context.chamado.status == status


@then("o chamado não deve possuir solução registrada")
def step_verificar_sem_solucao(context):
    assert context.chamado.solucao is None


@then("o chamado não deve possuir data de encerramento")
def step_verificar_sem_data_encerramento(context):
    assert context.chamado.data_encerramento is None