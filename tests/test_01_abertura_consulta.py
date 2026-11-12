import pytest
from src.service import ChamadoService


@pytest.fixture
def service():
    return ChamadoService()



def test_abrir_chamado_valido(service):
    chamado = service.abrir_chamado("Erro no Wi-Fi", "Sem acesso na sala 2", "Alta")
    assert chamado.id == 1
    assert chamado.titulo == "Erro no Wi-Fi"
    assert chamado.status == "Aberto"
    assert chamado.prioridade == "Alta"


def test_abrir_chamado_incrementa_id(service):
    c1 = service.abrir_chamado("Chamado 1", "Desc 1")
    c2 = service.abrir_chamado("Chamado 2", "Desc 2")
    assert c1.id == 1
    assert c2.id == 2


def test_abrir_chamado_sem_titulo_falha(service):
    with pytest.raises(ValueError, match="título"):
        service.abrir_chamado("   ", "Descrição")


def test_abrir_chamado_prioridade_invalida_falha(service):
    with pytest.raises(ValueError, match="Prioridade inválida"):
        service.abrir_chamado("Erro", "Descrição", "Urgentissima")



def test_buscar_chamado_existente(service):
    criado = service.abrir_chamado("Teclado quebrado", "Tecla Enter presa")
    encontrado = service.buscar_chamado(criado.id)
    assert encontrado.id == criado.id
    assert encontrado.titulo == "Teclado quebrado"


def test_buscar_chamado_inexistente_falha(service):
    with pytest.raises(ValueError, match="não encontrado"):
        service.buscar_chamado(999)