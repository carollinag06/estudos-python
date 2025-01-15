nNotas=int(input('Quantas notas vc quer analisar: '))

notas=0

for z in range(1, nNotas+1):
    nota=float(input(f'digite a {z}º nota: '))
    notas+=nota

print('_-'*25)

if notas/nNotas >= 7:
    print('Parabéns! Você está acima da média.')
elif 5 <= notas/nNotas < 7:
    print('Você está de recupoeração!')
else:
    print('Voce reprovou! Estude mais!')

print(f'A media das notas digitadas foi de: {notas/nNotas :.1f}')