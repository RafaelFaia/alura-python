# Marina trabalha no setor de segurança de uma empresa e precisa verificar se um determinado conjunto de permissões faz parte das permissões principais de um sistema. Sua tarefa é desenvolver um programa que receba duas listas de permissões e verifique se a segunda lista está contida na primeira.

permissoes_principais = set(input("Permissões principais: ").lower().split(','))
permissoes_solicitadas = set(input("Permissões solicitadas: ").lower().split(','))

permissoes_principais = {permissao.strip() for permissao in permissoes_principais}
permissoes_solicitadas = {permissao.strip() for permissao in permissoes_solicitadas}

eh_subconjunto = permissoes_solicitadas <= permissoes_principais  # Poderia ser expresso com permissoes_solicitadas.issubset(permissoes_principais)

if eh_subconjunto:  
    print("As permissões solicitadas fazem parte das permissões principais.")  
else:  
    print("As permissões solicitadas não fazem parte das permissões principais.")