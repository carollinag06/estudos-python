from turtledemo.penrose import start

numero=int(input('digite o numero que vc deseja ver a tabuada: '))

for x in range(1, 11):
    print('{} x {:2} = {}' .format(numero, x, numero*x))