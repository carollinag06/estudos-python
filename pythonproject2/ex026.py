from typing import Tuple

# Definindo constantes para o número de participantes
NUM_PARTICIPANTES = 4


def obter_dados_participante(c: int) -> Tuple[str, int, str]:

    while True:
        nome = input(f'Nome da {c}º pessoa: ').strip().lower()
        idade = input(f'Idade da {c}º pessoa: ')
        sexo = input(f'Sexo [M/F] da {c}º pessoa: ').strip().lower()

        # Validação de idade e sexo
        if not idade.isdigit() or int(idade) <= 0:
            print("Idade inválida. Tente novamente.")
            continue
        if sexo not in ['m', 'f']:
            print("Sexo inválido. Tente novamente.")
            continue

        return nome, int(idade), sexo


def analisar_participantes() -> None:

    media_idade = 0
    maior_idade_homem = {'nome': '', 'idade': -float('inf')}
    total_mulher_20 = 0

    for c in range(1, NUM_PARTICIPANTES + 1):
        nome, idade, sexo = obter_dados_participante(c)
        media_idade += idade

        if sexo == 'm':
            # Atualiza o homem mais velho
            if idade > maior_idade_homem['idade']:
                maior_idade_homem = {'nome': nome, 'idade': idade}
        elif sexo == 'f' and idade < 20:
            total_mulher_20 += 1

    # Exibindo os resultados
    media_idade /= NUM_PARTICIPANTES
    print(f'\nA média de idade dos participantes é de: {media_idade:.1f} anos.')
    print(
        f'O homem mais velho tem {maior_idade_homem["idade"]} anos e seu nome é {maior_idade_homem["nome"].capitalize()}.')
    print(f'{total_mulher_20} mulheres têm menos de 20 anos.')


if __name__ == "__main__":
    print("Analisador completo")
    analisar_participantes()
