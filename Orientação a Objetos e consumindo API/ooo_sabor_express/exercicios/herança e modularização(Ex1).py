class Banco:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

# Apenas informativo quando a criacação for em outro arquivo
# from banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome,endereco)
        self.mumero = numero