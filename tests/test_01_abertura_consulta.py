import pytest
from src.service import ChamadoService


@pytest.fixture
def service():
    return ChamadoService()


def test_abrir_chamado_valido(service):
    chamado = service.abrir_chamado("Erro no sistema", "Descrição", "Alta")
    assert chamado.id == 1
    assert chamado.titulo == "Erro no sistema"
    assert chamado.status == "Aberto"
    assert chamado.prioridade == "Alta"


def test_abrir_chamado_incrementa_id(service):
    c1 = service.abrir_chamado("Erro no sistema", "Descrição", "Alta")
    c2 = service.abrir_chamado("Monitor sem sinal", "Descrição", "Media")
    assert c1.id == 1
    assert c2.id == 2


def test_abrir_chamado_sem_titulo_falha(service):
    with pytest.raises(ValueError, match="O título do chamado é obrigatório."):
        service.abrir_chamado("", "Descrição")


def test_abrir_chamado_prioridade_invalida_falha(service):
    with pytest.raises(ValueError, match="Prioridade inválida."):
        service.abrir_chamado("Erro no sistema", "Descrição", "Urgentissima")


def test_buscar_chamado_existente(service):
    criado = service.abrir_chamado("Monitor sem sinal", "Descrição padrão", "Media")
    encontrado = service.buscar_chamado(criado.id)
    assert encontrado.id == 1
    assert encontrado.titulo == "Monitor sem sinal"


def test_buscar_chamado_inexistente_falha(service):
    with pytest.raises(ValueError, match="Chamado 999 não encontrado."):
        service.buscar_chamado(999)