import random
import string

def efeite ():
    print('_'*50)
def efeite1 ():
    print('-_-' *20)

print('Bem-vindo ao Gerador de Senhas Fortes!')
efeite1()

opcao1=input('Escolha uma opção:\n'
      '[1] Gerar nova senha \n'
      '[2] Sair\n'
      'Digite aqui sua opção: ')

efeite1()

if opcao1 == '1':
    comprimento=int(input('Digite o comprimento da senha (mínimo 8): '))
    while comprimento < 8:
        print('Digite um numero maior ou igual a 8.')
        comprimento = int(input('Digite o comprimento da senha (mínimo 8): '))
    efeite()

    LMaior=input('Incluir letras maiúsculas? (s/n): ')
    while LMaior != 's' and LMaior != 'n':
        print('Digite apenas s ou n.')
        LMaior = input('Incluir letras maiúsculas? (s/n): ')
    efeite()

    Lmenor=input('Incluir letras minúsculas? (s/n): ')
    while Lmenor != 's' and Lmenor != 'n':
        print('Digite apenas s ou n.')
        Lmenor = input('Incluir letras minúsculas? (s/n): ')
    efeite()

    numeros= input('Incluir números? (s/n): ')
    while numeros != 's' and numeros != 'n':
        print('Digite apenas s ou n.')
        numeros = input('Incluir números? (s/n): ')
    efeite()

    carEspe= input('Incluir caracteres especiais? (s/n): ')
    while carEspe != 's' and carEspe != 'n':
        print('Digite apenas s ou n.')
        carEspe = input('Incluir caracteres especiais? (s/n): ')

    efeite1()

    caracteres= ''
    if LMaior == 's':
        caracteres += string.ascii_uppercase
    if Lmenor == 's':
        caracteres+= string.ascii_lowercase
    if numeros == 's':
        caracteres+= string.digits
    if carEspe == 's':
        caracteres+=string.punctuation


    if caracteres:
        senha=''.join(random.choices(caracteres, k=comprimento))
        print(senha)

else:
    print('Gerador de senhas encerrado')
    efeite1()