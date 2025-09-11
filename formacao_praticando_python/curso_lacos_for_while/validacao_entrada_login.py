# João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:
# O nome de usuário deve ter pelo menos 5 caracteres.
# A senha deve ter pelo menos 8 caracteres.
# João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".
# Crie um programa que implemente essa lógica usando um laço while.

nome_usuario = ''
senha_usuario = ''

while True:
    nome_usuario = input('Digite seu nome de usuário: ')
    if len(nome_usuario) >= 5:
        break
    print('O nome de usuário deve ter pelo menos 5 caracteres.')

while True:
    senha_usuario = input('Digite sua senha: ')
    if len(senha_usuario) >= 8:
        break
    print('A senha deve ter pelo menos 8 caracteres.')

print('Cadastro realizado com sucesso!')