from cliente import Cliente 

class Conta:
    def __init__(self, saldo, numero, agencia, Cliente, historic=None):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = Cliente
        self._historic = historic if historic is not None else []

    @classmethod
    def nova_conta(cliente: Cliente, numero: int):
        pass
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente

    @property
    def historic(self): 
        return self._historic   
    
    def sacar(self, valor: float):
        if valor > self._saldo:
            print("Saldo insuficiente")
            return False
        self._saldo -= valor
        self._historic.append(f"Saque: {valor}")
        return True
    
    def depositar(self, valor: float):
        self._saldo += valor
        self._historic.append(f"Depósito: {valor}")
        return True
