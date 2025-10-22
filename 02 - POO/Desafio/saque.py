from transacao import Transacao
from conta import Conta

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta: Conta):
        sucesso = conta.sacar(self._valor)
        if sucesso:
            print(f"Saque de {self._valor} realizado com sucesso.")
        else:
            print(f"Saque de {self._valor} falhou devido a saldo insuficiente")
