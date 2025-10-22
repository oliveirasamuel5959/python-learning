from cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento):
        super().__init__()
        self._nome = nome
        self._cpf = cpf
        self._data_nascimento = data_nascimento