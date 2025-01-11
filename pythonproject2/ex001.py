from random import randint
from time import sleep

nA=randint(1, 5)
C=int(input('digite um numero de 1 a 5: '))
if C >5:
    C=int(input('digite um numero de 1 a 5: '))

print('processando...')
sleep(3)
print('=-='*20)
print(f'voce acertou eu pensei no numero: {nA}' if C==nA else f'Voce errou eu pensei no numero: {nA}')
