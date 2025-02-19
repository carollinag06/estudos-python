'''from math import factorial
num=int(input('Digite um numero: '))
print(f'O fatorial de {num} é: {factorial(num)}')'''

num = int(input('Digite um numero: '))
cont = 1
soma = 1
while cont < num:
    cont += 1
    soma = cont * soma
print(f'O fatorial de {num} é: {soma}')
