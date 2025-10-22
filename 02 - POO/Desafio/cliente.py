from pessoa_fisica import PessoaFisica
from transacao import Transacao
from conta import Conta

class Cliente(PessoaFisica):
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta: Conta, transacao: Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta: Conta):
        self._contas.append(conta)