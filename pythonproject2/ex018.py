print('Soma ímpares múltiplos de três')

x = 0
contador = 0

for c in range(3, 501, 3):
    if c % 2 != 0:
        x += c
        contador += 1

print(f'A soma de todos os {contador} múltiplos de 3 ímpares é igual a {x}')
