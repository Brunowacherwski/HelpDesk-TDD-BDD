from datetime import datetime
import pytest
from src.service import ChamadoService

DATA_ATUAL_SISTEMA = datetime.strptime("17/11/2026", "%d/%m/%Y")


@pytest.fixture
def service():
    return ChamadoService()


# --- Testes de encerrar_chamado (Mesma massa do Gherkin) ---

def test_encerrar_chamado_aberto_com_solucao_e_data_atual(service):
    chamado = service.abrir_chamado("Falha no servidor de e-mail", "Descrição padrão", "Alta")
    encerrado = service.encerrar_chamado(chamado.id, "Serviço SMTP reiniciado", DATA_ATUAL_SISTEMA)

    assert encerrado.status == "Fechado"
    assert encerrado.solucao == "Serviço SMTP reiniciado"
    assert encerrado.data_encerramento == DATA_ATUAL_SISTEMA


def test_encerrar_chamado_sem_solucao_falha(service):
    chamado = service.abrir_chamado("Falha no servidor de e-mail", "Descrição padrão", "Alta")
    with pytest.raises(ValueError, match="A solução do chamado é obrigatória."):
        service.encerrar_chamado(chamado.id, "", DATA_ATUAL_SISTEMA)

    assert chamado.status == "Aberto"
    assert chamado.data_encerramento is None


def test_encerrar_chamado_ja_fechado_falha(service):
    chamado = service.abrir_chamado("Troca de monitor", "Descrição padrão", "Media")
    service.encerrar_chamado(chamado.id, "Monitor trocado", DATA_ATUAL_SISTEMA)

    with pytest.raises(ValueError, match="Chamado #1 já está fechado."):
        service.encerrar_chamado(chamado.id, "Nova troca", DATA_ATUAL_SISTEMA)


def test_encerrar_chamado_inexistente_falha(service):
    with pytest.raises(ValueError, match="Chamado 999 não encontrado."):
        service.encerrar_chamado(999, "Serviço SMTP reiniciado", DATA_ATUAL_SISTEMA)


# --- Testes de reabrir_chamado ---

def test_reabrir_chamado_fechado_com_sucesso(service):
    chamado = service.abrir_chamado("Queda de rede no 2º andar", "Descrição padrão", "Media")
    service.encerrar_chamado(chamado.id, "Switch reiniciado", DATA_ATUAL_SISTEMA)

    reaberto = service.reabrir_chamado(chamado.id)

    assert reaberto.status == "Aberto"
    assert reaberto.solucao is None
    assert reaberto.data_encerramento is None


def test_reabrir_chamado_aberto_falha(service):
    chamado = service.abrir_chamado("Queda de rede no 2º andar", "Descrição padrão", "Media")
    with pytest.raises(ValueError, match="Apenas chamados fechados podem ser reabertos."):
        service.reabrir_chamado(chamado.id)


def test_reabrir_chamado_inexistente_falha(service):
    with pytest.raises(ValueError, match="Chamado 999 não encontrado."):
        service.reabrir_chamado(999)