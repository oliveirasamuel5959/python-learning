class Passaro:
    def voar(self):
        return "O pássaro está voando."
    
class Pardal(Passaro):
    def voar(self):
        return "O pardal está voando rapidamente."
    
class Avestruz(Passaro):
    def voar(self):
        return "A avestruz não pode voar."

# FIXME: Exemplo de polimorfismo com uma classe não relacionada
# TODO: Adicionar uma classe Aviao que também implemente o método voar
class Aviao(Passaro):
    def voar(self):
        return "O avião está voando."
    
def plano_de_voo(passaro: Passaro):
    return passaro.voar()
    
pardal = Pardal()
avestruz = Avestruz()
aviao = Aviao()
print(plano_de_voo(pardal))
print(plano_de_voo(avestruz))
print(plano_de_voo(aviao))