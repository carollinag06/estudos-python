#Jogo do Par ou Ímpar
from random import randint

vitorias = 0

while True:
    computador = randint(0, 10)

    while True:
        op_jogador = input('Você quer ímpar ou par? ').strip().lower()
        if op_jogador in ['par', 'ímpar', 'impar']:
            break
        print("Opção inválida! Escolha 'par' ou 'ímpar'.")

    num_jogador = int(input('Jogue um número: '))
    resultado = num_jogador + computador

    print('-' * 40)
    print(f'Você jogou {num_jogador}, eu joguei {computador}. A soma foi {resultado}.')

    if (op_jogador == 'par' and resultado % 2 == 0) or (op_jogador in ['ímpar', 'impar'] and resultado % 2 != 0):
        vitorias += 1
        print('Você venceu! 🎉 Vamos jogar de novo...')
        print('-' * 40)
    else:
        print('Você perdeu! 😢')
        print('-' * 40)
        break

print(f'Fim de jogo! Você venceu {vitorias} vezes.')
