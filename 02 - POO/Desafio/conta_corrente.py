from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite: float, limite_saques: int):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques