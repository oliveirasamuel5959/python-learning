from transacao import Transacao

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor