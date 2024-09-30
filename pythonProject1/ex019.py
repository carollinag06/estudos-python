import random

numeAlunos = int(input('Quantos alunos vão ser sorteados? '))

lista = []

for c in range(numeAlunos):
    nomeAlunos = str(input('Nome do {}º aluno: '.format(c+1)))
    lista.append(nomeAlunos)

soAluno = random.choice(lista)

print('O aluno que irá apagar o quadro hoje será: {}'.format(soAluno))
