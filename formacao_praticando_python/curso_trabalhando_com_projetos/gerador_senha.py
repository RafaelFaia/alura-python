# Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.
# Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada.

import random
import string

def gerar_senha():
    maiusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    especiais = "!@#$%&*"
    
    senha = [
        random.choice(maiusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiais)
    ]
    
    todos_caracteres = maiusculas + minusculas + numeros + especiais
    
    senha.extend(random.choices(todos_caracteres, k=8))
    
    random.shuffle(senha)
    
    return ''.join(senha)

print(f"Senha gerada: {gerar_senha()}")
