print('Verificação de Números Primos')

n = int(input('Digite um número: '))
contador = 0
if n == 1:
    print('O número 1 não é primo, pois um número primo deve ter exatamente dois divisores: 1 e ele mesmo.')
else:
    for c in range(1, n+1):
        if n % c == 0:
            contador += 1


    if contador == 2:
        print(f'O número {n} é primo, pois ele só é divisível por 1 e por ele mesmo.')
    else:
        print(f'O número {n} não é primo, pois ele tem {contador} divisores.')

