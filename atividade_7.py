altura = float(input('Digite sua altura: '))

print(f'Se você for homem seu peso ideal é {(72.7*altura)-58:.2f} \n'
      f'Se você for mulher seu pedo ideal é {(62.1*altura)-44.7:.2f}')

lado = float(input("Digite o valor do lado do quadrado: "))
area = lado ** 2
print(f"A área do quadrado é: {area}")
print(f"O dobro da área do quadrado é: {area * 2:.2f}")



tempo_em_C = float(input('Digite a temperatura em Celsius: '))
print(f'{(tempo_em_C * 1.8) + 32:.2f} Fahrenheit.')

metros = int(input("Digite uma média em metros: "))
cm = metros * 100
print(f"A média de {metros} metos e centímetros é: {cm}")

tempo_em_F = float(input('Digite a temperadra em Fahrenheit: '))
print(f'{(tempo_em_F - 32) / 1.8:.2f} Celsius.')

altura = float(input("Digite sua altura: "))
print(f'O seu peso ideial é {(altura * 72.7) -58:.2f}')

num1 = [int(input('Digite um numero inteiro: ')) for x in range(2)]
num_real = float(input("Digite um número real: "))

print(f"O produto do dobro do primeiro com metade do segundo é {(num1[0] * 2) * (num1[1] / 2)}")

print(f"A soma do triplo do primeiro com o terceiro é: {3 * num1[0] + num_real}")

print(f"O terceiro elevado ao cubo é {num_real ** 3:.2f}")

r = float(input("Qual é o raio do circulo: "))
print("A área do circulo é: {}".format (r**2 * 3.14159))

salario_por_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas_mes = float(input('Digite quantas horas você trabalha por mês: '))

print(f'Você recebe R${salario_por_hora * horas_trabalhadas_mes:.2f} por mês.')
