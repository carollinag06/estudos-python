import random

print('Bem-vindo ao Gerador de Senhas Fortes!')
print('-_-' *20)

opcao1=input('Escolha uma opção:\n'
      '[1] Gerar nova senha \n'
      '[2] Sair\n'
      'Digite aqui sua opção: ')

print('-_-' *20)

if opcao1 == '1':
    comprimento=input('Digite o comprimento da senha (mínimo 8): ')
    LMaior=input('Incluir letras maiúsculas? (s/n): ')
    Lmenor=input('Incluir letras minúsculas? (s/n): ')
    numeros= input('Incluir números? (s/n): ')
    carEspe= input('Incluir caracteres especiais? (s/n): ')

    print(random.choice())