import random

Qalunos=int(input('Quantos alunos vao participar do sorteio? '))

lista= []
for x in range(1, Qalunos+1):
    alunos=str(input('Digite o nome do aluno: '))
    lista.append(lista)


print('O aluno sorteado foi o {}' .format(random.choice(lista)))
