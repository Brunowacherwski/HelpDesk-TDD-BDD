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