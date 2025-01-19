print('Grupo da Maioridade')

from datetime import date

maior = 0
menor = 0

for c in range(1, 8):
    nascimento = int(input(f'Ano de nascimento da {c}º pessoa: '))
    idade = date.today().year - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} são maior de idade \n'
      f'{menor} são menor de idade')
