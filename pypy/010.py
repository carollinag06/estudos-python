#Simulador de Caixa Eletrônico

valor=int(input('Valor a ser sacado: '))
total=valor

while total >= 100:
    n100=total/100

while total >= 20:
    n20=total/20

while total >= 10:
    n10=total/10

while total >= 1:
    n1=total/1

if valor >= 100:
    print(f'Total de {n100} notas de R$100')