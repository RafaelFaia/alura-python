# Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.
# Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.

operacoes = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else 'Erro: Divisão por zero'
}

x = float(input('Digite o primeiro número: ')) 
y = float(input('Digite o segundo número: ')) 
operacao = input('Escolha a operação (| + | - | * | / |): ') 

if operacao in operacoes:  
    resultado = operacoes[operacao](x, y)  
    print(f'O resultado é: {resultado}')  
else:  
    print('Operação inválida')