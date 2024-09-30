Qkm = float(input('Quantos km vc percorreu com o carro? '))
Qdias = int(input('Quantos dias vc ficou com o carro? '))

dia = 60*Qdias
kmR = 0.15*Qkm

print('Você terá que pagar o total de {}' .format(dia + kmR))
