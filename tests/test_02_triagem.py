import pytest
from src.service import ChamadoService


@pytest.fixture
def service():
    return ChamadoService()


# --- Testes de cadastrar_prioridade (Mesma massa do Gherkin) ---

def test_cadastrar_prioridade_valida(service):
    prioridades = service.cadastrar_prioridade("Critica")
    assert "Critica" in prioridades


def test_cadastrar_prioridade_vazia_falha(service):
    with pytest.raises(ValueError, match="O nome da prioridade é obrigatório."):
        service.cadastrar_prioridade("")


def test_cadastrar_prioridade_duplicada_falha(service):
    with pytest.raises(ValueError, match="Prioridade já cadastrada."):
        service.cadastrar_prioridade("Alta")


# --- Testes de atribuir_tecnico (Mesma massa do Gherkin) ---

def test_atribuir_tecnico_muda_status_para_em_andamento(service):
    chamado = service.abrir_chamado("Impressora sem conexão", "Descrição padrão", "Media")
    atualizado = service.atribuir_tecnico(chamado.id, "Carlos")
    assert atualizado.tecnico == "Carlos"
    assert atualizado.status == "Em Andamento"


def test_atribuir_tecnico_vazio_falha(service):
    chamado = service.abrir_chamado("Impressora sem conexão", "Descrição padrão", "Media")
    with pytest.raises(ValueError, match="O nome do técnico é obrigatório."):
        service.atribuir_tecnico(chamado.id, "")


def test_atribuir_tecnico_chamado_fechado_falha(service):
    chamado = service.abrir_chamado("Mouse quebrado", "Descrição padrão", "Baixa")
    chamado.status = "Fechado"
    with pytest.raises(ValueError, match="Chamado #1 já está fechado."):
        service.atribuir_tecnico(chamado.id, "Carlos")


def test_atribuir_tecnico_chamado_inexistente_falha(service):
    with pytest.raises(ValueError, match="Chamado 999 não encontrado."):
        service.atribuir_tecnico(999, "Carlos")


# --- Testes de alterar_prioridade (Mesma massa do Gherkin) ---

def test_alterar_prioridade_chamado_aberto(service):
    chamado = service.abrir_chamado("Sistema lento", "Descrição padrão", "Baixa")
    atualizado = service.alterar_prioridade(chamado.id, "Alta")
    assert atualizado.prioridade == "Alta"


def test_alterar_prioridade_para_nova_prioridade_cadastrada(service):
    service.cadastrar_prioridade("Critica")
    chamado = service.abrir_chamado("Sistema lento", "Descrição padrão", "Baixa")
    atualizado = service.alterar_prioridade(chamado.id, "Critica")
    assert atualizado.prioridade == "Critica"


def test_alterar_prioridade_chamado_fechado_falha(service):
    chamado = service.abrir_chamado("Teclado falhando", "Descrição padrão", "Baixa")
    chamado.status = "Fechado"
    with pytest.raises(ValueError, match="Chamado #1 já está fechado."):
        service.alterar_prioridade(chamado.id, "Alta")


def test_alterar_prioridade_invalida_falha(service):
    chamado = service.abrir_chamado("Sistema lento", "Descrição padrão", "Baixa")
    with pytest.raises(ValueError, match="Prioridade inválida."):
        service.alterar_prioridade(chamado.id, "Inexistente")