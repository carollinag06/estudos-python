# Fibonacci v1.0

num = int(input('Primeiro número da sequência: '))
fim = int(input('Quantos números você quer na sequência? '))

anterior = num
proximo = num
cont = 0

if num == 0:
    proximo=1

while cont < fim:
    print(anterior, end=', ')
    temporario = anterior + proximo
    anterior = proximo
    proximo = temporario
    cont += 1

print('FIM')