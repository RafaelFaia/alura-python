# Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.
# Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:
# Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
# Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.
 
try:
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif operacao == "-":
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif operacao == "*":
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif operacao == "/":
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Operação inválida!")
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
