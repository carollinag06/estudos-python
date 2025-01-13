print('Calculando IMC')

peso=float(input('Seu peso: '))
altura=float(input('Sua altura: '))/100

if peso/(altura*altura) <=   18.4:
    print('Você está abaixo do peso!')

elif 18.5 <= peso/(altura * altura) <= 24:
    print('Você está na sua faixa de peso ideal!')

elif 25 <= peso/(altura*altura) <= 30:
    print('Você está com sobrepeso!')

print(f'Seu IMC é de: {peso/(altura*altura) :.2f}')