pessoa = {
    "nome": "Carlos",
    "idade": 28,
    "cidade": "São Paulo"
}
print(pessoa)

pessoa["idade"] = 29
print(pessoa)

pessoa["profissao"] = "Engenheiro"
print(pessoa)

del pessoa["cidade"]
print(pessoa)

quadrados = {x: x**2 for x in range(1, 6)}
print(quadrados)

dados = {"nome": "Ana", "idade": 25, "cidade": "Rio de Janeiro"}
chave = "idade"

if chave in dados:
    print(f"A chave '{chave}' existe no dicionário.")
else:
    print(f"A chave '{chave}' não existe no dicionário.")

frase = "programação é prática prática prática"
palavras = frase.split()
frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(frequencia)
