# Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

# Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.

dias_atividade_a = int(input("Informe os dias para a atividade A: "))
dias_atividade_b = int(input("Informe os dias para a atividade B: "))
dias_atividade_c = int(input("Informe os dias para a atividade C: "))

if dias_atividade_a < 0 or dias_atividade_b < 0 or dias_atividade_c < 0:
    print("Erro: Os dias não podem ser negativos.")
else:
    print(f"O tempo total do projeto é de {dias_atividade_a + dias_atividade_b + dias_atividade_c} dias.")