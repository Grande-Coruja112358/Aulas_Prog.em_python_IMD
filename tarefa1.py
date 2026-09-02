#Questão 1)
numero = int(input("Digite o seu número: "))
if numero == 0:
  print(f' Zero. ')
  if numero == 1:
  print(f' Um. ')
  if numero == 2:
  print(f' Dois. ')
  if numero == 3:
  print(f' Três. ')
  if numero == 4:
  print(f' Quatro. ')
  if numero == 5:
  print(f' Cinco. ')
  if numero == 6:
  print(f' Seis. ')
  if numero == 7:
  print(f' Sete. ')
  if numero == 8:
  print(f' Oito. ')
  if numero == 9:
  print(f' Nove. ')

# Questão 2)
x = input("Digite a operação: ")
if x =="!":
    n = int(input("Digite o único número a ser utilizado: "))
else:
    n = int(input("Digite um número:"))
    m = int(input("Digite um outro número:"))

if x == "+":
    res = n + m
elif x == "-":
    res = n - m
elif x == "x":
    res = n * m
elif x == "*":
    res = n * m
elif x == "/":
    res = n / m
elif x == ":":
    res = n / m 

print(f' {res}')

#Questão 3
peso = float(input("Digite o seu peso (em quilos): "))
altura = float(input("Digite a sua altura (em metros): "))
IMC = peso / altura ** 2

print(f' {IMC}')
print(f' ==================')

if IMC < 18.5:
  print(f' Abaixo do peso')
elif IMC < 25:
  print(f' Peso Normal')
elif IMC < 30:
  print(f' Sobre Peso')
elif IMC < 35:
  print(f' Obesidade Grau I')
elif IMC < 40:
  print(f' Obesidade grau II')
else:
  print(f' Obesidade Mórbida')
print(f' ==================')
