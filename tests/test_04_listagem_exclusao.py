import pytest
from src.service import ChamadoService


@pytest.fixture
def service():
    return ChamadoService()


def test_filtrar_chamados_por_status_ordena_alta_no_topo(service):
    c1 = service.abrir_chamado("Trocar mouse", "Descrição padrão", "Baixa")
    c1.status = "Aberto"

    c2 = service.abrir_chamado("Servidor fora do ar", "Descrição padrão", "Alta")
    c2.status = "Aberto"

    c3 = service.abrir_chamado("Erro antigo", "Descrição padrão", "Alta")
    c3.status = "Fechado"

    resultados = service.filtrar_chamados(status="Aberto")

    assert len(resultados) == 2
    assert resultados[0].titulo == "Servidor fora do ar"
    assert resultados[0].prioridade == "Alta"
    assert resultados[1].titulo == "Trocar mouse"
    assert resultados[1].prioridade == "Baixa"


def test_filtrar_chamados_por_prioridade(service):
    c1 = service.abrir_chamado("Trocar mouse", "Descrição padrão", "Baixa")
    c1.status = "Aberto"

    c2 = service.abrir_chamado("Dúvida no sistema", "Descrição padrão", "Media")
    c2.status = "Aberto"

    resultados = service.filtrar_chamados(prioridade="Media")

    assert len(resultados) == 1
    assert resultados[0].titulo == "Dúvida no sistema"
    assert resultados[0].prioridade == "Media"


def test_excluir_chamado_com_status_aberto(service):
    chamado = service.abrir_chamado("Monitor sem sinal", "Descrição padrão", "Media")
    chamado.status = "Aberto"

    service.excluir_chamado(1)

    with pytest.raises(ValueError, match="Chamado 1 não encontrado."):
        service.buscar_chamado(1)


def test_impedir_exclusao_de_chamado_que_nao_esta_aberto(service):
    chamado = service.abrir_chamado("Falha na rede", "Descrição padrão", "Alta")
    chamado.status = "Em Andamento"

    with pytest.raises(
        ValueError,
        match="O chamado #1 possui status 'Em Andamento'. Apenas chamados 'Abertos' podem ser excluídos.",
    ):
        service.excluir_chamado(1)


def test_impedir_exclusao_de_chamado_inexistente(service):
    with pytest.raises(ValueError, match="Chamado 999 não encontrado."):
        service.excluir_chamado(999)