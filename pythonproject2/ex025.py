print('Maior e menor da sequência')

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Digite o peso da {c}º pessoa: '))
    if c == 1:
        maior=peso
        menor=peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'\nMaior peso: {maior} \n'
      f'Menor peso: {menor}')
