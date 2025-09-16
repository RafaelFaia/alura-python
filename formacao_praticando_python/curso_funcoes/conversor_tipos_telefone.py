# Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.
# Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:

telefones = ['11987654321', '21912345678', '31987654321', '11911223344'] 

def converter_para_inteiro(telefones):
    return [int(telefone) for telefone in telefones]

def verificar_conversao(telefones):
    return all(isinstance(telefone,int) for telefone in telefones)

telefones_convertidos = converter_para_inteiro(telefones)
print('Telefones convertidos:', telefones_convertidos)
print('Todos são inteiros?', 'Sim' if verificar_conversao(telefones_convertidos) else 'Não')