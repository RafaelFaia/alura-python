# O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.
# Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

resultados = ['Ana', 'Carlos', 'Pedro']
print('Lista original:', resultados)

nome_errado = input('Digite o nome incorreto: ')
if nome_errado in resultados:
    nome_correto = input('Digite o nome correto: ')
    posicao = resultados.index(nome_errado)
    resultados.remove(nome_errado)
    resultados.insert(posicao, nome_correto)
    print(f'O nome {nome_errado} foi substituído por {nome_correto}.')
    print('Lista atualizada:', resultados)
else:
    print('Nome não encontrado.')