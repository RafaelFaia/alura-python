
# Laura e Ana resolveram fazer compras juntas, mas criaram duas listas diferentes. Elas querem um programa que mostre:
# Quais itens apareceram nas duas listas
# Quais foram exclusivos de Laura
# Quais foram exclusivos da Ana
# Escreva um programa que solicite as listas e mostre os resultados dessas comparações.

lista_laura = set(input('Lista de Laura: ').split(','))
lista_ana = set(input('Lista de Ana: ').split(','))

itens_comuns = lista_laura & lista_ana  # Poderia ser expresso com lista_laura.intersection(lista_ana)
itens_exclusivos_laura = lista_laura - lista_ana  # Poderia ser expresso com lista_laura.difference(lista_ana)
itens_exclusivos_ana = lista_ana - lista_laura  # Poderia ser expresso com lista_ana.difference(lista_laura)

print(f'Itens em ambas as listas: {', '.join(itens_comuns)}')
print(f'Itens exclusivos de Laura: {', '.join(itens_exclusivos_laura)}')
print(f'Itens exclusivos de Ana: {', '.join(itens_exclusivos_ana)}')