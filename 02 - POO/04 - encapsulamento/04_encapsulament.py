class Conta:
    def __init__(self, saldo, num_agencia):
        self._saldo = saldo # atributo protegido
        self.num_agencia = num_agencia
    
    def sacar(self, valor):
        if valor > self._saldo:
            print("Saldo insuficiente!")
        else:
            self._saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")

    def depositar(self, valor):
        self._saldo += valor
        print(f"Depósito de {valor} realizado com sucesso.")

    def get_saldo(self):
        return self._saldo


conta = Conta(1000, 0o001)
conta.depositar(500)  # Depósito de 500
conta.sacar(200)  # Saque de 200
print(f"Saldo final: {conta.get_saldo()}")  # Saldo final: 1300