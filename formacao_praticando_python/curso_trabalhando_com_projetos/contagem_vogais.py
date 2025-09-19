# Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.
# Crie um programa que peça um texto e exiba quantas vogais (a, e, i, o, u) ele contém.

vogais = "aeiou"  
quantidade = 0  

texto = input("Digite um texto: ") 

for letra in texto.lower():  
    if letra in vogais:  
        quantidade += 1  

print(f"O texto contém {quantidade} vogais.") 