#Vários números com flag

lista=[]
total=0

while True:
    num=int(input('digite um numero: '))
    print('- '*20)

    if num==999:
        break

    total+=num
    lista.append(num)

print(f'A soma dos : {len(lista)} numeros digitados, fica:{total} ')


