numero = int(input("Digite um número: "))
11
if numero %2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'o numero {numero} é ímpar')


idade = int(input('Digite sua idade: '))

if idade < 12:
    print(f'Você é uma criança com {idade} anos')
elif 13 <= idade <= 18:
    print(f'Você é um Adolescente com {idade} anos')
else:
    print(f'Você é um adulto com {idade} anos')


nome_u_v = 'nome_u_v'
senha_v = 'senha_v'

nome_u_d = input('Digite seu nome: ')
senha_d = input('Digite sua senha: ')

if (nome_u_v == nome_u_d) and (senha_v == senha_d):
    print('Login efetudado com sucesso1')
else:
    print('Nome de usuário ou senha inválidos.')



x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x > 0 and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x < 0 and y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")