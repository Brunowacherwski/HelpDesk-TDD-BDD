x   import pytest
from src.service import ChamadoService

@pytest.fixture
def service():
    svc = ChamadoService()
    svc.abrir_chamado("Problema no mouse", "Não clica", "Baixa") # ID 1
    svc.abrir_chamado("Servidor caído", "Fora do ar", "Alta")     # ID 2
    svc.abrir_chamado("Dúvida de acesso", "Esqueci a senha", "Media") # ID 3
    return svc

def test_filtrar_chamados_ordena_alta_no_topo(service):
    resultados = service.filtrar_chamados()
    assert resultados[0].prioridade == "Alta"
    assert resultados[1].prioridade == "Media"
    assert resultados[2].prioridade == "Baixa"

def test_filtrar_chamados_por_status(service):
    # Simulando um chamado fechado
    chamado_fechado = service.buscar_chamado(1)
    chamado_fechado.status = "Fechado"
    
    resultados = service.filtrar_chamados(status="Aberto")
    assert len(resultados) == 2
    assert todos_sao_abertos(resultados)

def test_filtrar_chamados_por_prioridade(service):
    resultados = service.filtrar_chamados(prioridade="Alta")
    assert len(resultados) == 1
    assert resultados[0].id == 2

def test_excluir_chamado_aberto(service):
    service.excluir_chamado(1) # O chamado 1 nasce como 'Aberto'
    with pytest.raises(ValueError, match="não encontrado"):
        service.buscar_chamado(1)

def test_excluir_chamado_diferente_de_aberto_falha(service):
    chamado = service.buscar_chamado(2)
    chamado.status = "Em Andamento" # Modificando para forçar a falha
    
    with pytest.raises(ValueError, match="Apenas chamados 'Abertos' podem ser excluídos"):
        service.excluir_chamado(2)

# Função auxiliar para o teste
def todos_sao_abertos(chamados):
    return all(c.status == "Aberto" for c in chamados)