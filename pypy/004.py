#Maior e Menor valores

lista=[]
total=0

while True:
    num=int(input('digite um numero: '))
    continuar=input('deseja continuar? [S/N]: ').lower()
    print('_-'*20)
    total+=num
    lista.append(num)

    if continuar == 'n':
        break


print(f'Média: {total/len(lista):.2f}')
print(f'Maior valor: {max(lista)}')
print(f'Menor valor: {min(lista)}')


