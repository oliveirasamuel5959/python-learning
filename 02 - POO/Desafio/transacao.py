from abc import ABC, abstractmethod
from conta import Conta

class Transacao(ABC):

    @property
    @classmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta: Conta):
        pass