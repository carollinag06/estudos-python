pessoa = {"nome": "Ana", "idade": 22, "cidade": "Curitiba"}
pessoa["profissao"] = "Designer"  # Adiciona nova chave

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")