# Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.
# Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.

def contador_caracteres(palavra):
    print(f'Essa palavra tem {len(palavra)} caracteres')

contador_caracteres(input('Digite uma palavra: '))