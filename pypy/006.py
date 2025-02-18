#Tabuada v3.0
from unicodedata import numeric

while True:
    num=int(input('Você quer ver a tabuada de qual numero: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c:2} = {num*c}')

print('FIM')