# Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.
# Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

texto = input('Digite um texto: ').split()

palavras_longas = []
for palavra in texto:
    if len(palavra) > 10 and palavra not in palavras_longas:
        palavras_longas.append(palavra)

if palavras_longas:
    print(f'Palavras longas encontradas: {', '.join(palavras_longas)}')
else:  
    print('Nenhuma palavra longa foi encontrada no texto.')