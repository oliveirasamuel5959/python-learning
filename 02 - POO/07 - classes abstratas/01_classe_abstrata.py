from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod    
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")

    def desligar(self):
        print("Desligando a TV")


class ControleRadio(ControleRemoto):
    def ligar(self):
        print("Ligando o Rádio")
    
    def desligar(self):
        print("Desligando o Rádio")

c = ControleTV()
c.ligar() 
c.desligar() 