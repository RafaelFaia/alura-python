# Paula trabalha em uma plataforma de ensino online e precisa garantir que os alunos sejam inscritos corretamente nos cursos desejados. O sistema deve seguir as seguintes regras:
# Cada aluno pode se inscrever em um curso, mas antes a plataforma precisa verificar se há vagas disponíveis;
# Se houver vagas, o aluno deve ser confirmado na turma e a vaga deve ser reduzida;
# Se não houver vagas, o aluno deve ser notificado de que a turma está lotada;
# Se um aluno já estiver inscrito, ele não pode se inscrever novamente no mesmo curso.
# A lista de alunos e os cursos disponíveis já está definida no sistema. Lembre-se de processar múltiplas inscrições em paralelo. Confira o código:
# cursos = {
#     'Python Avançado': {'vagas': 2, 'inscritos': []},
#     'Java para Iniciantes': {'vagas': 1, 'inscritos': []},
#     'Machine Learning': {'vagas': 0, 'inscritos': []},
# }
# alunos = [
#     {'nome': 'Alice', 'curso': 'Python Avançado'},
#     {'nome': 'Bruno', 'curso': 'Python Avançado'},
#     {'nome': 'Carlos', 'curso': 'Java para Iniciantes'},
#     {'nome': 'Daniela', 'curso': 'Machine Learning'},
#     {'nome': 'Alice', 'curso': 'Python Avançado'},  # Tentativa de inscrição duplicada
# ]

import asyncio

cursos = {
    'Python Avançado': {'vagas': 2, 'inscritos': []},
    'Java para Iniciantes': {'vagas': 1, 'inscritos': []},
    'Machine Learning': {'vagas': 0, 'inscritos': []},
}

alunos = [
    {'nome': 'Alice', 'curso': 'Python Avançado'},
    {'nome': 'Bruno', 'curso': 'Python Avançado'},
    {'nome': 'Carlos', 'curso': 'Java para Iniciantes'},
    {'nome': 'Daniela', 'curso': 'Machine Learning'},
    {'nome': 'Alice', 'curso': 'Python Avançado'},
]

# Criar um lock para cada curso individualmente
curso_locks = {curso: asyncio.Lock() for curso in cursos}

async def inscrever_aluno(aluno):
    nome_aluno = aluno['nome']
    curso_desejado = aluno['curso']
    
    print(f'Inscrevendo {nome_aluno} no curso {curso_desejado}...')

    if curso_desejado not in cursos:
        print(f'Erro! O curso {curso_desejado} não existe.\n')
        return

    # Usar o lock específico para este curso
    async with curso_locks[curso_desejado]:
        nome_curso = cursos[curso_desejado]

        if nome_aluno in nome_curso['inscritos']:
            print(f'{nome_aluno} já está inscrito no curso {curso_desejado}! Inscrição rejeitada.\n')
            return

        if nome_curso['vagas'] > 0:
            nome_curso['inscritos'].append(nome_aluno)
            nome_curso['vagas'] -= 1
            print(f'Inscrição confirmada para {nome_aluno} no curso {curso_desejado}!\n')
        else:
            print(f'Turma lotada! {nome_aluno} não pôde se inscrever no curso {curso_desejado}.\n')

async def main():
    tarefas = [asyncio.create_task(inscrever_aluno(aluno)) for aluno in alunos]
    await asyncio.gather(*tarefas)
    print('Todas as inscrições foram processadas!\n')

asyncio.run(main())