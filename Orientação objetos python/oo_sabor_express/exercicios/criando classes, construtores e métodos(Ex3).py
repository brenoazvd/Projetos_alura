class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False  # A conta começa inativa por padrão

    def __str__(self):
        return f'Titular: {self.titular}, Saldo: R${self.saldo:.2f}'

conta1 = ContaBancaria('Alice', 1500.0)
conta2 = ContaBancaria('Bob', 2500.0)

print(conta1)
print(conta2)

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'Titular: {self.titular}, Saldo: R${self.saldo:.2f}'

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True
conta3 = ContaBancaria('Carlos', 3000.0)
ContaBancaria.ativar_conta(conta3)
print(conta3.ativo)  # Deve retornar True

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self.saldo = saldo
        self.ativo = False

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if not valor:
            raise ValueError("O titular não pode ser vazio.")
        self._titular = valor

    def __str__(self):
        return f'Titular: {self.titular}, Saldo: R${self.saldo:.2f}'

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

conta4 = ContaBancaria('Diego', 4000.0)
print(conta4.titular)  # Exibe o titular da conta

class ClienteBanco:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

cliente1 = ClienteBanco('Ana', 30, '12345678900', 'Rua A, 100', '(11) 1111-1111')
cliente2 = ClienteBanco('Bruno', 25, '98765432100', 'Rua B, 200', '(21) 2222-2222')
cliente3 = ClienteBanco('Carla', 28, '55566677700', 'Rua C, 300', '(31) 3333-3333')

class ClienteBanco:
    def __init__(self, nome, idade, cpf, endereco, telefone):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone

    @classmethod
    def saudacao_cliente(cls, cliente):
        return f'Olá {cliente.nome}, obrigado por ser nosso cliente!'

print(ClienteBanco.saudacao_cliente(cliente1))
