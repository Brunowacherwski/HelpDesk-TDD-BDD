from datetime import datetime
from typing import List, Optional

from src.models import Chamado, PRIORIDADES_VALIDAS


STATUS_ABERTO = "Aberto"
STATUS_EM_ANDAMENTO = "Em Andamento"
STATUS_FECHADO = "Fechado"

class ChamadoService:
    def __init__(self):
        self._chamados: List[Chamado] = []
        self._proximo_id: int = 1
        self._prioridades: List[str] = list(PRIORIDADES_VALIDAS)

    # ================= INTEGRANTE 1 =================
    def abrir_chamado( self, titulo: str, descricao: str, prioridade: str = "Media", solicitante: Optional[str] = None) -> Chamado:
        if not titulo or not titulo.strip():
            raise ValueError("O título do chamado é obrigatório.")
        if prioridade not in PRIORIDADES_VALIDAS:
            raise ValueError("Prioridade inválida.")

        chamado = Chamado(
            id=self._proximo_id,
            titulo=titulo.strip(),
            descricao=descricao.strip() if descricao else "",
            prioridade=prioridade,
            solicitante=solicitante,
        )
        self._chamados.append(chamado)
        self._proximo_id += 1
        return chamado

    def buscar_chamado(self, chamado_id: int) -> Chamado:
        for chamado in self._chamados:
            if chamado.id == chamado_id:
                return chamado

        raise ValueError(f"Chamado {chamado_id} não encontrado.")


    # ================= INTEGRANTE 2  =================
    def cadastrar_prioridade(self, nova_prioridade: str) -> List[str]:
        if not nova_prioridade or not nova_prioridade.strip():
            raise ValueError("O nome da prioridade é obrigatório.")

        prioridade_limpa = nova_prioridade.strip()
        if any(p.lower() == prioridade_limpa.lower() for p in self._prioridades):
            raise ValueError("Prioridade já cadastrada.")

        self._prioridades.append(prioridade_limpa)
        return self._prioridades

    def atribuir_tecnico(self, chamado_id: int, tecnico: str) -> Chamado:
        chamado = self.buscar_chamado(chamado_id)
        if chamado.status == STATUS_FECHADO:
            raise ValueError(f"Chamado #{chamado_id} já está fechado.")
        if not tecnico or not tecnico.strip():
            raise ValueError("O nome do técnico é obrigatório.")

        chamado.tecnico = tecnico.strip()
        chamado.status = STATUS_EM_ANDAMENTO
        return chamado

    def alterar_prioridade(self, chamado_id: int, nova_prioridade: str) -> Chamado:
        chamado = self.buscar_chamado(chamado_id)
        if chamado.status == STATUS_FECHADO:
            raise ValueError(f"Chamado #{chamado_id} já está fechado.")
        if not nova_prioridade or nova_prioridade.strip() not in self._prioridades:
            raise ValueError("Prioridade inválida.")

        chamado.prioridade = nova_prioridade.strip()
        return chamado

    # ================= INTEGRANTE 3  =================

    def encerrar_chamado(
            self,
            chamado_id: int,
            solucao: Optional[str],
            data_encerramento: Optional[datetime] = None,
    ) -> Chamado:
        chamado = self.buscar_chamado(chamado_id)
        if chamado.status == "Fechado":
            raise ValueError(f"Chamado #{chamado_id} já está fechado.")
        if not solucao or not solucao.strip():
            raise ValueError("A solução do chamado é obrigatória.")

        chamado.solucao = solucao.strip()
        chamado.data_encerramento = data_encerramento or datetime.now()
        chamado.status = "Fechado"
        return chamado

    def reabrir_chamado(self, chamado_id: int) -> Chamado:
        chamado = self.buscar_chamado(chamado_id)
        if chamado.status != "Fechado":
            raise ValueError("Apenas chamados fechados podem ser reabertos.")

        chamado.solucao = None
        chamado.data_encerramento = None
        chamado.status = "Aberto"
        return chamado

    # ================= INTEGRANTE 4  =================

    def filtrar_chamados(self, status: str = None, prioridade: str = None) -> List[Chamado]:
        resultado = self._chamados

        if status:
            resultado = [c for c in resultado if c.status == status]
        if prioridade:
            resultado = [c for c in resultado if c.prioridade == prioridade]

        pesos_prioridade = {"Alta": 0, "Media": 1, "Baixa": 2}

        resultado = sorted(resultado, key=lambda c: pesos_prioridade.get(c.prioridade, 99))

        return resultado

    def excluir_chamado(self, chamado_id: int) -> None:
        chamado = self.buscar_chamado(chamado_id)

        if chamado.status != "Aberto":
            raise ValueError(f"O chamado #{chamado_id} possui status '{chamado.status}'. Apenas chamados 'Abertos' podem ser excluídos.")

        self._chamados.remove(chamado)