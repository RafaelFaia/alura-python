# Você trabalha em uma biblioteca e está organizando os títulos de livros no sistema. Você precisa identificar todos os títulos que possuem palavras iniciadas por uma determinada letra, para criar coleções temáticas baseadas em letras específicas. Por exemplo, você poderia usar isso para agrupar livros com palavras que começam com a mesma letra, ajudando na organização ou em campanhas como “Livros com A para você!”.
# Como você criaria um programa que solicita um texto e uma letra inicial e retorna todas as palavras do texto que começam com essa letra?

import re

titulo_livro = input('Digite o título dos livro: ')
letra_escolhida = input('Digite a letra inicial para pesquisa: ')
palavras = re.findall(rf'\b{letra_escolhida}[a-zà-ÿ]*', titulo_livro, re.IGNORECASE)
print(palavras)