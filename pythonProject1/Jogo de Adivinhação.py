import random

def enfeite ():
    print('--' *30)

print('Seja bem vindo ao: Jogo de Adivinhação com Dificuldade Variável')

nivel=int(input('Em qual nivel de dificuldade você quer jogar? \n'
                '[1] nivel facil\n'
                '[2] nivel medio\n'
                '[3] nivel dificil\n'
                'Digite aqui sua resposta: '))
enfeite()

if nivel == 1:
    print('Seja bem-vindo ao nivel facil!')
    numero1=random.randint(1, 10)
    tentativa=int(input('Tente adivinhar o numero: '))
    while True:
        if numero1 > tentativa:
            enfeite()
            print('Seu chute foi muito baixo')
        if numero1 < tentativa:
            enfeite()
            print('Seu chute foi muito alto')
        if numero1 == tentativa:
            enfeite()
            print('Você acertou! Eu também pensei no número {}'.format(numero1))
            break
        tentativa = int(input('Tente novamente: '))

if nivel == 2:
    print('Seja bem-vindo ao nivel facil!')
    numero2=random.randint(1, 50)
    tentativa=int(input('Tente adivinhar o numero: '))
    while True:
        if numero2 > tentativa:
            enfeite()
            print('Seu chute foi muito baixo')
        if numero2 < tentativa:
            enfeite()
            print('Seu chute foi muito alto')
        if numero2 == tentativa:
            enfeite()
            print('Você acertou! Eu também pensei no número {}'.format(numero2))
            break
        tentativa = int(input('Tente novamente: '))

if nivel == 3:
    print('Seja bem-vindo ao nivel facil!')
    numero3=random.randint(1, 100)
    tentativa=int(input('Tente adivinhar o numero: '))
    while True:
        if numero3 > tentativa:
            enfeite()
            print('Seu chute foi muito baixo')
        if numero3 < tentativa:
            enfeite()
            print('Seu chute foi muito alto')
        if numero3 == tentativa:
            enfeite()
            print('Você acertou! Eu também pensei no número {}'.format(numero3))
            break
        tentativa = int(input('Tente novamente: '))
