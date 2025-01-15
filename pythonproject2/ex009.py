n1=int(input('Digite o 1º valor: '))
n2=int(input('Digite o 2º valor: '))

maior=n1

if n2 > n1:
    maior=n2
elif n1 == n2:
    print('O primeiro número é equivalente ao segundo')

print(f'O maior numero digitado foi: {maior}')