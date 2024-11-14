print('Seja bem vindo ao programa para cadastrar e buscar alunos')

opcao1 = int(input('O que você deseja fazer hj?\n'
                   '[1] Cadastrar um usuario\n'
                   '[2] Sair\n'
                   'Digite aqui sua opção: '))

lista = []
while True:

    if opcao1 == 1:
        aluno = {}
        aluno["nome"] = input('Qual é o nome do usuario? ')
        aluno["turma"] = input('Qual turma? ')
        lista.append(aluno)
        continuar = input('deseja continuar? ')

        if continuar == 'n':
            break
        print('- ' * 30)

for aluno in lista:
    print(aluno)
