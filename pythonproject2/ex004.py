d=int(input('distancia percorrida: '))

print(f'O preço da passagem será de: R${d*0.50 :.2f}' if d <= 200 else
      f'O preço da passagem será de: R${d*0.45 :.2f}')
print('Boa viajem!')