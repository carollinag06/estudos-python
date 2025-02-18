#Tratando vários valores v1.0
lista=[]
soma=0
while True:
    num=int(input('Digite um número: '))
    if num == 999:
        break
    else:
        lista.append(num)
        soma+=num

print('Foram digitados',len(lista),'numeros')
print('A soma de todos eles deu: ',soma)