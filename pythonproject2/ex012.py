from datetime import date

# Solicita o ano de nascimento do atleta
nascimento = int(input('Digite o ano de nascimento do atleta: '))
# Calcula a idade do atleta
idade = date.today().year - nascimento

# Classifica o atleta com base na idade
if idade <= 9:
    print('Atleta mirim')

elif idade <= 14:
    print('Atleta infantil')

elif idade <= 19:
    print('Atleta júnior')

elif idade <= 25:
    print('Atleta sênior')

else:
    print('Atleta master')
