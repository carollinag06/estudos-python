print('Gerenciador de Pagamentos')

produto = float(input('Preço do produto: R$'))

while True:
    fp = int(input('Qual será a forma de pagamento: \n'
                   '[1] à vista dinheiro/cheque: 10% de desconto \n'
                   '[2] à vista no cartão: 5% de desconto \n'
                   '[3] em até 2x no cartão: preço formal  \n'
                   '[4] 3x ou mais no cartão: 20% de juros \n'
                   'Sua resposta: '))
    print('-=-' * 20)
    if fp in [1, 2, 3, 4]:  # Verifica se a opção é válida
        break  # Se a opção for válida, sai do loop
    else:
        print("Opção inválida, por favor, insira uma opção válida.")

if fp == 1:
    preco_final = produto - (produto * 10 / 100)

elif fp == 2:
    preco_final = produto - (produto * 5 / 100)

elif fp == 3:
    preco_final = produto

else:
    preco_final = (produto * 20 / 100) + produto

print(f'O valor final do produto ficará: R${preco_final}')
