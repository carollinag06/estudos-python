print('Progressão Aritmética')

primeiro=int(input('Priomeiro termo da PA: '))
intervalo=int(input('Intervalo da PA:'))
soma=primeiro

for c in range(1, 11):
    print(soma, end=' → ')
    soma+=intervalo

print('FIM')