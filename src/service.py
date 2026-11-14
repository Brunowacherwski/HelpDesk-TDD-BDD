from datetime import datetime
from typing import List, Optional

from src.models import Chamado, PRIORIDADES_VALIDAS

STATUS_ABERTO = "Aberto"
STATUS_FECHADO = "Fechado"

class ChamadoService:

    def __init__(self):
        self._chamados: List[Chamado] = []
        self._proximo_id: int = 1

    def abrir_chamado(
            self, titulo: str, descricao: str, prioridade: str = "Media",
            solicitante: Optional[str] = None) -> Chamado:
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