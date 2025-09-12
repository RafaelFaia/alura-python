# Imagine que você precisa criar uma funcionalidade para um jogo, onde os jogadores recebem dicas baseadas em partes específicas de uma palavra-chave. Sua missão é desenvolver um programa que extraia trechos importantes de qualquer palavra digitada.
# Escreva um programa que solicite ao usuário uma palavra e exiba as três primeiras e as três últimas letras.

palavra = input('Digite uma palabra chave: ')
print(f'Primeiras: {palavra[:3]}')
print(f'últimas: {palavra[-3:]}')