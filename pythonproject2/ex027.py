#Validação de Dados

sexo = str(input('Informe o sexo: [F/M] ')).strip().lower()
while sexo not in ['m', 'f']:
    sexo = str(input('Informe um sexo válido: [F/M] '))

if sexo == 'f':
    print(f'Sexo feminino registrado com sucesso!')
else:
    print(f'Sexo masculino registrado com sucesso!')
