from random import choice

# definindo funções
def main():
    print('GAME: Pedra Papel e Tesoura')
    print('-'*35)
    jogar()

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']

    #logica do jogo
    while True:
        maquina = choice(opcoes)
        while True:
            jogador = input('O que você jogou? ').lower()
            if jogador in opcoes:
                break
            else:
                print('Opção inválida')

        # verifica vencedor
        if jogador == maquina:
            print(f'Deu empate! Eu também joguei {maquina}')
        elif (jogador == 'pedra' and maquina == 'tesoura') or \
             (jogador == 'tesoura' and maquina == 'papel') or \
             (jogador == 'papel' and maquina == 'pedra'):
            print(f'Você venceu! Eu joguei {maquina}.')
        else:
            print(f'Eu venci! Eu joguei {maquina}.')

        print('-=-'*15)

        while True:
            continua = input('Você quer jogar novamente? [S/N]: ').strip().lower()
            if continua == 's':
                break
            elif continua == 'n':
                print('Até a próxima!')
                return  # Sai da função e termina o jogo
            else:
                print('Opção inválida, digite [S] para sim ou [N] para não.')

# Iniciar o jogo
main()
