print('Olá, essa é a lista de tarefa super master')
print('-' * 42)

print('O que vc deseja:\n'
      '[1] criar tarefas\n'
      '[2] editar tarefas\n'
      '[3] excluir tarefas')

resposta = input('Digita o número da sua opção aqui: ')

listatarefas = { }

if resposta == '1':
    tarefa = input('Digite o nome da sua tarefa: ')
    listatarefas.append(tarefa)

if resposta == '2':
    editar1=input('qual é a terefa que vc deseja editar? ')
    editar2= input('insira aqui oq vc deseja colocar no lugar: ')



print(listatarefas)