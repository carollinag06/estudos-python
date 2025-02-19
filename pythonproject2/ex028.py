from random import randint

print('Jogo da Adivinhação v2.0')
computador = randint(1, 10)
cont = 1
jogador = int(input("Tente adivinhar qual é o número: "))
print(computador)

while True:
    if jogador == computador:
        print('-=-' * 20)
        print(f"Parabéns, você acertou! O número era {computador}.")
        if cont == 1:
            print("Incrível! Você acertou de primeira! 🏆")
        else:
            print(f"Você precisou de {cont} tentativa(s), mas conseguiu! 🎉")
        print('-=-' * 20)
        break

    else:
        print('-' * 60)
        if jogador < computador:
            print("O número é maior... Tente novamente! ⬆️")
        elif jogador > computador:
            print("O número é menor... Tente novamente! ⬇️")

    jogador = int(input("Qual é o seu próximo palpite? "))
    cont += 1
