from time import sleep

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

while True:
    print("\nEscolha uma opção:")
    opcoes = int(input('   [ 1 ] Somar\n'
                       '   [ 2 ] Multiplicar\n'
                       '   [ 3 ] Mostrar o maior\n'
                       '   [ 4 ] Inserir novos números\n'
                       '   [ 5 ] Sair do programa\n'
                       '>>>> Sua opção: '))

    if opcoes == 1:
        resultado = num1 + num2
        print(f'\nA soma de {num1} + {num2} é {resultado}.')
        print('-' * 40)
        sleep(3)
    elif opcoes == 2:
        resultado = num1 * num2
        print(f'\nA multiplicação de {num1} x {num2} é {resultado}.')
        print('-' * 40)
        sleep(3)
    elif opcoes == 3:
        if num1 > num2:
            print(f'\nO maior número entre {num1} e {num2} é {num1}.')
        elif num2 > num1:
            print(f'\nO maior número entre {num1} e {num2} é {num2}.')
        else:
            print(f'\nAmbos os números são iguais: {num1}.')
        print('-' * 40)
        sleep(3)
    elif opcoes == 4:
        print('\nVocê escolheu inserir novos números.')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
        print('-' * 40)
    elif opcoes == 5:
        print('\nObrigado por usar o programa! Até logo!')
        break
    else:
        print('\nOpção INVÁLIDA! Por favor, escolha uma opção válida.')
        print('-' * 40)
