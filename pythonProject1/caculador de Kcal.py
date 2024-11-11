nome=input('Qual o seu nome: ')
caminhada_leve = int(3.5)
corrida_moderada = int(8.5)
pular_corda = int(12)

Nome_ativ=input('Qual atividade fisica você deseja inserir? \n'
      '[1] Caminhada leve \n'
      '[2] Corrida moderada\n'
      '[3] Pular corda \n'
      'Digite aqui sua opção: ')

tempo_ativ=int(input('Quantos minutos durou sua atividade fisica: '))

if Nome_ativ == '1':
    resultado= caminhada_leve*tempo_ativ
    print('\nOlá {}, você gastou {}kcal em {} minutos de Caminhada leve.' .format(nome, resultado, tempo_ativ))

if Nome_ativ == '2':
    resultado= corrida_moderada*tempo_ativ
    print('\nOlá {}, você gastou {}kcal em {} minutos de Corrida moderada.' .format(nome, resultado, tempo_ativ))

if Nome_ativ == '3':
    resultado= pular_corda*tempo_ativ
    print('\nOlá {}, você gastou {}kcal em {} minutos Pulando corda.' .format(nome, resultado, tempo_ativ))