
def somaImposto(taxaImposto, custo):
    imposto = custo * (taxaImposto / 100)
    custo_total = custo + imposto
    return custo_total

taxa = float(input("Digite a taxa de imposto sobre vendas: "))
valor_custo = float(input("Digite o custo do item antes do imposto: "))

valor_final = somaImposto(taxa, valor_custo)
print("O valor final do item, incluindo imposto, é:", valor_final)

def contarDigitos(frase):
    quantidade_digitos = sum(char.isdigit() for char in frase)
    return quantidade_digitos

frase = input("Digite uma frase: ")
digitos = contarDigitos(frase)
print("A quantidade de dígitos na frase é:", digitos)

def reversoNumero(numero):
    reverso = int(str(numero)[::-1])
    return reverso

numero = int(input("Digite um número inteiro: "))
reverso = reversoNumero(numero)
print("O reverso do número é:", reverso)
