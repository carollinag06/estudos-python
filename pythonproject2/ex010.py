from datetime import date

sexo=str(input('Qual é seu sexo? Feminino = F / Masculino = M : ')).lower().strip()

if sexo == 'm':
    ano_nascimento=int(input('Em que ano vc nasceu? '))
    if date.today().year - ano_nascimento < 18:
        print(f'Ainda não esta na hora de vc se alistar, faltam {18-(date.today().year-ano_nascimento)} anos!')
    elif date.today().year - ano_nascimento == 18:
        print('Você deve se alistar esse ano!')
    else:
        print(f'Você deveria ter se alistado há {(date.today().year-ano_nascimento)-18} anos')

else:
    print('Você não precisa se alistar você é mulher!')