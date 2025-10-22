class Foo:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, novo_valor):
        self._valor += novo_valor

    @valor.deleter
    def valor(self):
        self._valor = 0
    

foo = Foo(42)
print(foo.valor)  # Acessa o valor via propriedade, saída: 42
foo.valor = 100  # Tenta modificar o valor diretamente (isso causará um erro)  # AttributeError: can't set attribute
print(foo.valor)  # Acessa o valor novamente via propriedade, saída: 142
del foo.valor  # Tenta deletar o valor diretamente (isso causará um erro)  # AttributeError: can't delete attribute
print(foo.valor)  # Acessa o valor novamente via propriedade, saída: 142