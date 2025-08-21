# 1 - Crie uma lista para cada informação a seguir:
# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_de_nomes = ['Marilda', 'Jurandir', 'Rafael', 'Renata']
lista_de_anos = [1999, 2025]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in lista_de_numeros:
    print(numero)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
soma_impares = 0
for numero_impar in range(1,11,2):
    soma_impares += numero_impar
print(soma_impares)

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
for numero in range (10, 0, -1):
    print(numero)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
numero_escolhido = int(input('Digite um numero para a tabuada: '))
for i in range(1, 11):
    print(f'{numero_escolhido} x {i} = {numero_escolhido * i}')

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_dos_numeros = 0
try:
    for numero in lista_de_numeros:
        soma_dos_numeros += numero
    print(f"Soma dos elementos: {soma_dos_numeros}")
except Exception as e:
    print(f'Ocorreu um erro: {e}')

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma_dos_numeros = 0
try:
    for numero in lista_de_numeros:
        soma_dos_numeros += numero
    media_dos_numeros = soma_dos_numeros / len(lista_de_numeros)
    print(f'Média dos valores: {media_dos_numeros}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média')
except Exception as e:
    print(f'Ocorreu um erro: {e}')