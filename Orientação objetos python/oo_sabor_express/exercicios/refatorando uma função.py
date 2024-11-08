class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = int(idade)
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, sua profissão é {self.profissao}'

    def aniversario(self):
        """Incrementa a idade da pessoa em 1 ano."""
        self.idade += 1


    @property
    def saudacao(self):
        """Retorna uma saudação personalizada com base na profissão."""
        return f'Olá {self.nome}, como está o trabalho de {self.profissao}?'


miguel_pessoa = Pessoa('Miguel', 19, 'Pedreiro')

# Exibindo as variáveis da instância
print(vars(miguel_pessoa))

# Chamando o método aniversario
miguel_pessoa.aniversario()
print(f"Após aniversário: {miguel_pessoa.idade} anos")

# Usando a propriedade saudacao
print(miguel_pessoa.saudacao)