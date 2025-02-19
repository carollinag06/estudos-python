print('Progressão Aritmética 2.0')

primeiro = int(input('Primeiro termo da PA: '))
intervalo = int(input('Intervalo da PA: '))
soma = primeiro
cont = 0

while cont < 10:
    print(soma, end=' → ')
    soma = intervalo + soma
    cont += 1

print('FIM')
