# Número por Extenso

numeros = ['um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte']


n = int(input('Digite um número entre 1 e 20 para ver por extenso: '))

if 1 <= n <= 20:
    print(f'O número {n} por extenso é: {numeros[n-1]}.')
else:
    print('Por favor, digite um número válido entre 1 e 20.')
