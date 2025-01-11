s=float(input('Salario do funcionario: '))

print(f'O salario que é {s}, passara a ser {(s * 10) / 100 + s :.2f}' if s > 1518 else
      f'O salario que é {s}, passara a ser {(s*15)/100 + s :.2f}')