#Maior e Menor valores

num=int(input('digite um numero: '))
continuar=input('deseja continuar? [S/N]: ').lower()
print('_-'*20)

lista=[]
total=num
cont=1

while True:
    num=int(input('digite um numero: '))
    continuar=input('deseja continuar? [S/N]: ').lower()
    print('_-'*20)
    cont += 1
    total+=num
    lista.append(num)
    if continuar == 'n':
        break

media=total/cont

print(f'Média: {media}')
print(f'Maior valor: {max(lista)}')
print(f'Menor valor: {min(lista)}')


