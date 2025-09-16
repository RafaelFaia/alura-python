# Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.
# Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.

vendas_realizadas = input('Digite os valores das vendas: ').split()
total_de_vendas = sum(map(float,vendas_realizadas))
print(f'O total de vendas foi: {total_de_vendas}')