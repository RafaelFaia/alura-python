# Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.
# Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().

lista_de_numeros = input('Digite os números separados por espaço: ').split()
lista_de_numeros_pares = filter(lambda x: int(x) % 2 == 0, lista_de_numeros)
print(f'Números pares: {' '.join(lista_de_numeros_pares)}')