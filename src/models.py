from dataclasses import dataclass
from datetime import datetime
from typing import Optional

PRIORIDADES_VALIDAS = ("Baixa", "Media", "Alta")
STATUS_VALIDOS = ("Aberto", "Em Andamento", "Fechado")


@dataclass
class Chamado:
    id: int
    titulo: str
    descricao: str
    prioridade: str = "Media"
    status: str = "Aberto"
    tecnico: Optional[str] = None
    solucao: Optional[str] = None
    data_encerramento: Optional[datetime] = None