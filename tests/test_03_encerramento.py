import pytest
from src.service import ChamadoService


def test_encerrar_chamado_com_sucesso():
    service = ChamadoService()
    chamado = service.abrir_chamado("Teste", "Descrição", "Media")
    chamado.status = "Em Andamento"

    service.encerrar_chamado(chamado.id, "Reinicialização do serviço de rede")

    assert chamado.status == "Fechado"
    assert chamado.solucao == "Reinicialização do serviço de rede"
    assert chamado.data_encerramento is not None


def test_reabrir_chamado_com_sucesso():
    service = ChamadoService()
    chamado = service.abrir_chamado("Teste", "Descrição", "Media")
    service.encerrar_chamado(chamado.id, "Solução aplicada")

    service.reabrir_chamado(chamado.id)

    assert chamado.status == "Aberto"
    assert chamado.solucao is None
    assert chamado.data_encerramento is None


def test_tentativa_reabrir_chamado_nao_fechado():
    service = ChamadoService()
    chamado = service.abrir_chamado("Teste", "Descrição", "Media")

    with pytest.raises(ValueError, match="Apenas chamados fechados podem ser reabertos"):
        service.reabrir_chamado(chamado.id)


def test_encerrar_chamado_sem_solucao_falha():
    service = ChamadoService()
    chamado = service.abrir_chamado("Teste", "Descrição", "Media")

    with pytest.raises(ValueError, match="solução"):
        service.encerrar_chamado(chamado.id, "   ")

    assert chamado.status == "Aberto"


def test_encerrar_chamado_ja_fechado_falha():
    service = ChamadoService()
    chamado = service.abrir_chamado("Teste", "Descrição", "Media")
    service.encerrar_chamado(chamado.id, "Solução aplicada")

    with pytest.raises(ValueError, match="já está fechado"):
        service.encerrar_chamado(chamado.id, "Outra solução")


def test_ciclo_completo_encerrar_reabrir_e_encerrar_novamente():
    service = ChamadoService()
    chamado = service.abrir_chamado("Teste", "Descrição", "Media")
    service.encerrar_chamado(chamado.id, "Solução aplicada")
    service.reabrir_chamado(chamado.id)

    service.encerrar_chamado(chamado.id, "Nova solução")

    assert chamado.status == "Fechado"
    assert chamado.solucao == "Nova solução"
