from typing import List
from src.models import Chamado, PRIORIDADES_VALIDAS


class ChamadoService:
    def __init__(self):
        self._chamados: List[Chamado] = []
        self._proximo_id: int = 1

    # ================= INTEGRANTE 1 =================

    def abrir_chamado(self, titulo: str, descricao: str, prioridade: str = "Media") -> Chamado:
        if not titulo or not titulo.strip():
            raise ValueError("O título do chamado é obrigatório.")
        if prioridade not in PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridade inválida. Use: {PRIORIDADES_VALIDAS}")

        chamado = Chamado(
            id=self._proximo_id,
            titulo=titulo.strip(),
            descricao=descricao.strip() if descricao else "",
            prioridade=prioridade,
        )
        self._chamados.append(chamado)
        self._proximo_id += 1
        return chamado

    def buscar_chamado(self, chamado_id: int) -> Chamado:
        for chamado in self._chamados:
            if chamado.id == chamado_id:
                return chamado
        raise ValueError(f"Chamado #{chamado_id} não encontrado.")

    # ================= INTEGRANTE 4  =================

    def filtrar_chamados(self, status: str = None, prioridade: str = None) -> List[Chamado]:
        """
        Filtra os chamados por status e/ou prioridade e ordena trazendo a prioridade 'Alta' no topo.
        """
        resultado = self._chamados

        if status:
            resultado = [c for c in resultado if c.status == status]
        if prioridade:
            resultado = [c for c in resultado if c.prioridade == prioridade]

        # Dicionário de pesos para ordenação (Alta no topo)
        pesos_prioridade = {"Alta": 0, "Media": 1, "Baixa": 2}

        # Ordena usando o peso definido. Prioridades desconhecidas vão para o fim.
        resultado = sorted(resultado, key=lambda c: pesos_prioridade.get(c.prioridade, 99))
        
        return resultado

    def excluir_chamado(self, chamado_id: int) -> None:
        """
        Remove um chamado da lista. Só permite se o status for 'Aberto'.
        """
        # Reaproveita a busca do Integrante 1, que já valida se o chamado existe
        chamado = self.buscar_chamado(chamado_id)

        if chamado.status != "Aberto":
            raise ValueError(f"O chamado #{chamado_id} possui status '{chamado.status}'. Apenas chamados 'Abertos' podem ser excluídos.")
        
        self._chamados.remove(chamado)