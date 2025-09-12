# Uma ONG está organizando uma campanha de arrecadação de alimentos e precisa registrar os nomes dos voluntários que vão ajudar na ação. À medida que os voluntários se inscrevem, seus nomes devem ser adicionados à lista e quando for digitado a palavra sair o programa deve encerrar.
# Ajude a ONG a criar um programa que permita registrar os voluntários e exiba a lista completa no final.

nome_voluntarios = []

while True:
    nome_voluntario = input('Digite o nome do voluntário (ou "sair" para encerrar): ')
    if nome_voluntario.lower() == 'sair':
        break
    nome_voluntarios.append(nome_voluntario)
print(f'Voluntários registrados: {nome_voluntarios}')