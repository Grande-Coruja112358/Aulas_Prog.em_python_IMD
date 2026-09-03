# Questão 1
a = 1
num1 = int(input("Digite o seu número: "))
while a < num1:
    print(f'{a}', end = ' ')
    a += 2
# Questão 2 
b = 3
contador = 0
while contador < 10:
    print(f'{b * contador}')
    contador += 1
# Questão 3
b = int(input("Digite o número: "))
contador = 1
while contador < 10:
    print(f' {b} x {contador} ={b * contador}', end = ' ')
    contador += 1 
# Questão 4
b = int(input("Digite o número: "))
c = int(input("Digite o seu número... de novo"))
contador = 1
while contador < c:
    print(f' {b} x {contador} ={b * contador}', end = ' ')
    contador += 1
# Questão 5
pontos = 0
questao = 1
while questao < 4:
    resposta = input(" Digite a sua resposta: ").lower()
    if questao == 1 and resposta == "b":
        pontos = pontos + 1
    elif questao == 2 and resposta == "a":
        pontos = pontos + 1
    elif questao == 3 and resposta == "d":
        pontos = pontos + 1
    questao += 1
print(f' O aluno fez {pontos} pontos. ')