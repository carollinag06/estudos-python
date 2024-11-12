import random

print('Seja bem vindo ao: Jogo de Adivinhação com Dificuldade Variável')

nivel=int(input('Em qual nivel de dificuldade você quer jogar? \n'
                '[1] nivel facil\n'
                '[2] nivel medio\n'
                '[3] nivel dificil\n'
                'Dgite aqui sua resposta: '))

if nivel == 1:
    numeroC=random.randint(1, 10)
    tentativa=int(input('Tente adivinhar o numero: '))
    if numeroC == tentativa:
        print('Você acertou! Eu também pensei no número {}' .format(numeroC))