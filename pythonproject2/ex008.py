x = str(print('Simulador de emprestimo'))
print('-=-'*10)

#definindo variaveis
valor_casa=int(input('Qual o valor da casa: '))
salario_comprador=int(input('quanto vc ganha: '))
tempo_pagar=int(input('Em quantos anos vc quer pagar: '))

if (salario_comprador*30)/100-salario_comprador > valor_casa/(tempo_pagar*12):
    print(f'Seu emprestido foi negado! As parcelas do emprestimo ficaram acima de 30% do seu salario \n'
          f'Seu salario: {salario_comprador}'
          f'Valor da parcela: {valor_casa/tempo_pagar :.2f}')

else:
    print(f'Seu empretimo foi aprovado! \n'
          f'Seu salario: {salario_comprador} \n'
          f'Valor da parcela: {valor_casa/tempo_pagar :.2f}')