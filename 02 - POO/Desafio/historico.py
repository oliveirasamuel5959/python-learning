from transacao import Transacao
from datetime import datetime

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao._valor,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        )