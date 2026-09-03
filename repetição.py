# Questão 1
x = 1
while x < 100:
    print(f'{x}', end = ' ')
    x = x + 1

# Questão 2
y = 50
while y < 100:
    print(f'{y}', end = ' ')
    y = y + 1 

# Questão 3
x1 = 10
while x1 >= 0:
    print(f'{x1}', end = ' ')
    x1 = x1 - 1
if x1 == -1:
    print(f'Fogo!')

# Questão Adicional
numero = int(input("Digite o seu número: "))
z  = 0
while z < numero:
    if z % 2 == 0:
        print(f'{z}', end = ' ')
    z = z + 1

pontos = 0
questao = 1
while questao < 4:
    resposta = input(" Digite a sua resposta: ")
    if questao == 1 and resposta == "b":
        pontos = pontos + 1
    elif questao == 2 and resposta == "a":
        pontos = pontos + 1
    elif questao == 3 and resposta == "d":
        pontos = pontos + 1
    questao += 1
print(f' O aluno fez {pontos} pontos. ')