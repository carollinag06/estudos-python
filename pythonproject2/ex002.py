velocidaC=int(input('digite a velocidade do carro: '))

if velocidaC > 80:
    print('você ecedeu o limite de velocidade')
    print('_-'*30)
    print(f'A multa será de: R${(velocidaC-80)*7}')

else:
    print('vc esta no limite de velocidade')