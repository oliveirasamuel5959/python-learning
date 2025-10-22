class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        return f"O motor do {self.__class__.__name__} foi ligado."
    
    def __str__(self):
        return f"Veículo: {self.__class__.__name__}, Cor: {self.cor}, Placa: {self.placa}, Número de Rodas: {self.numero_rodas}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        return f"{'Sim' if self.carregado else 'Não'}, o caminhão está carregado."




moto = Motocicleta("Honda", "CB500", 4)
# print(moto.ligar_motor())
carro = Carro("Toyota", "Corolla", 4)
# print(carro.ligar_motor())
caminhao = Caminhao("vermelho", "XFD-0055", 8, True)
# print(caminhao.ligar_motor())
# print(caminhao.esta_carregado())
print(moto)
print(carro)
print(caminhao) 