print('Progressão Aritmética 3.0')

primeiro = int(input('Primeiro termo da PA: '))
intervalo = int(input('Intervalo da PA: '))
limite = 10
soma = primeiro
cont = 0

while limite != 0:
    while cont < limite:
        print(soma, end=' → ')
        soma += intervalo
        cont += 1
    print('PAUSA')

    continuar = int(input('Quantos termos a mais vc quer mostrar? '))
    if continuar == 0:
        break
    limite += continuar
print(f'Progressão finalizada com {cont} termos mostrados.')

