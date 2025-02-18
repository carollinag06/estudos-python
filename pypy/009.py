#Estatísticas em produtos
produtos = {'nome': [], 'total': 0, 'maior_1000': 0, 'mais_barato': {'nome': '', 'preco': float('inf')}}

while True:
    nome = input('nome: ')
    preco = float(input('preço: R$'))
    continuar = input('continuar [S/N]: ').lower()
    print('- '*20)

    produtos['nome'].append(nome)
    produtos['total']+=preco

    if preco >= 999:
        produtos['maior_1000'] += 1

    if continuar == 'n':
        break

    if preco < produtos['mais_barato']['preco']:
        produtos['mais_barato']['preco'] = preco
        produtos['mais_barato']['nome'] = nome

print(f'Total gasto na compra: R${produtos["total"]}')
print(f'Tive {produtos["maior_1000"]} produtos que custam mais de R$1000 reais')
print(f'O produto mais barato é "{produtos["mais_barato"]["nome"]}" que custa R${produtos["mais_barato"]["preco"]} reais')