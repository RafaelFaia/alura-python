# Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.
# Crie um programa que peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.


cpf = input('Digite seu CPF: ')
if len(cpf) == 11:
    if cpf.isdigit():
        print('CPF válido.')
    else:
        print('Erro: O CPF deve conter apenas números.')
else:
    print('Erro: O CPF deve ter exatamente 11 dígitos.')
