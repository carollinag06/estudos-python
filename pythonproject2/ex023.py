print('Detector de Palíndromo')

frase = input('digite uma frase: ').lower() .replace(' ', '')
print('- ' * 30)
invertido=frase[:: -1]

if invertido == frase:
    print('É polimedro')
else:
    print('Não é polimedro')

print(f'O inverso de "{frase}" é: {invertido}')