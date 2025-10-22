class Estudante:
    escola = "Escola XYZ"  # Atributo de classe

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"Estudante: {self.nome}, Matrícula: {self.matricula}, Escola: {self.escola}"
    

def mostrar_valores():
    print(f"Atributo de classe 'escola': {Estudante.escola}")

aluno1 = Estudante("Ana", "2023001")
aluno2 = Estudante("Bruno", "2023002")

print(aluno1)
print(aluno2)

aluno1.matricula = "2023010"  # Modificando o atributo de instância
print(aluno1)