# Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.
# Crie um programa que junte as listas e exiba o resultado no formato produto: preço

lista_produtos = input('Digite os produtos separados por vírgula: ').split(', ')
lista_precos = input('Digite os preços separados por vírgula: ').split(', ')

for produto, preco in zip(lista_produtos,lista_precos):
    print(f'{produto}: {preco}')
