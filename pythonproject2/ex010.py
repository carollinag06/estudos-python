print('Alistamento Militar')

from datetime import date

sexo = input('Qual é seu sexo? Feminino = F / Masculino = M : ').lower().strip()

if sexo not in ['f', 'm']:
    print("Entrada inválida! Por favor, digite 'F' para Feminino ou 'M' para Masculino.")
else:
    if sexo == 'm':
        ano_nascimento = int(input('Em que ano você nasceu? '))
        idade = date.today().year - ano_nascimento

        if idade < 18:
            print(f'Ainda não está na hora de você se alistar, seu alistamento será em {(18-idade)+date.today().year}')
        elif idade > 18:
            print(f'Você deveria ter se alistado em {date.today().year-(idade - 18)} anos.')
        else:
            print('Você deve se alistar este ano!')
    else:
        print('Você não precisa se alistar, pois você é mulher.')
