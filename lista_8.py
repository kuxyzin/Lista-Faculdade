
num = float(input("Digite um número inteiro ou real:"))
if num > 10:
  print(f"{num} é maior que 10")
elif num ==10: 
  print(f"{num} é igual a 10")
else:
  print(f"{num} é menor que 10")

num = float(input("Digite um número: "))
if num >= 0:
  print(f'O número {num} é Positivo.')
else:
  print(f'O número {num} é Negativo.')

quantidade_maca = int(input('Quantas maçãs deseja comprar: '))
if quantidade_maca >= 12:
    print(f'{quantidade_maca} maçãs custam R${quantidade_maca * 1.00:.2f}')
else:
    print(f'{quantidade_maca} maçãs custam R${quantidade_maca * 1.30:.2f}')

nota1 = float(input("Digite sua 1ª nota: "))
nota2 = float(input("Digite sua 2º nota: "))
media = (nota1 + nota2) / 2
if (media) >= 6:
    print(f'Você foi aprovado com media {media}')
else:
    print(f'infelizmente você foi reprovado com média {media}')

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

while valor1 == valor2:
    print("Os valores não podem ser iguais. Digite novamente.")
    valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    print("O maior valor é:", valor1)
else:
    print("O maior valor é:", valor2)

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

while valor1 == valor2:
    print("Os valores não podem ser iguais. Digite novamente.")
    valor2 = float(input("Digite o segundo valor: "))
if valor1 > valor2:
    print(valor2, valor1,sep=" / ")
else:
    print(valor1, valor2, sep=" / ")

conta = int(input("Digite o número da conta do cliente: "))
saldo = float(input("Digite o saldo atual: "))
debito = float(input("Digite o valor do débito: "))
credito = float(input("Digite o valor do crédito: "))

saldo_atual = saldo - debito + credito

print("O saldo atual da conta é:", saldo_atual)

if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")

estoque_atual = int(input("Digite a quantidade atual em estoque: "))
estoque_maximo = int(input("Digite a quantidade máxima em estoque: "))
estoque_minimo = int(input("Digite a quantidade mínima em estoque: "))

quantidade_media = (estoque_maximo + estoque_minimo) / 2

print("A quantidade média em estoque é:", quantidade_media)

if estoque_atual >= quantidade_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9.0:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6.0:
    conceito = "C"
elif media >= 4.0:
    conceito = "D"
else:
    conceito = "E"

print(f"Notas: {nota1} e {nota2}")
print("Média: ", media)
print("Conceito: ", conceito)

if conceito in ["A", "B", "C"]:
    print("APROVADO")
else:
    print("REPROVADO")
