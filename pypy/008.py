pessoas = {'total': 0, 'homens': 0, 'mulheres': 0, 'maiores_18': 0}

while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ').strip().lower()

    if sexo == 'm':
        pessoas['homens'] += 1
    elif sexo == 'f':
        pessoas['mulheres'] += 1
    else:
        print('Sexo inválido! Por favor, digite "M" para masculino ou "F" para feminino.')
        continue

    if idade >= 18:
        pessoas['maiores_18'] += 1
    pessoas['total'] += 1

    continuar = input('Deseja continuar? [S/N]: ').strip().lower()
    print('- '*30)
    if continuar == 'n':
        break

print('\nResultados:')
print(f'Total de pessoas cadastradas: {pessoas["total"]}')
print(f'Total de homens: {pessoas["homens"]}')
print(f'Total de mulheres: {pessoas["mulheres"]}')
print(f'Total de pessoas maiores de 18 anos: {pessoas["maiores_18"]}')