import datetime

a = int(input('digite o ano que vc quer saber se é bissexto, ou digite 0 para ver seu ano atual: '))
anosB = []
anoU = []

for z in range(0, 9999, 4):
    anosB.append(z)

if a == 0:
    a = datetime.date.today().year

if a == 1900 or a % 2 != 0:
    print(f'O ano de {a} não foi um ano bissexto')

elif a % 2 == 0 and a != 1900:
    print(f'O ano de {a} foi um ano bissexto')

