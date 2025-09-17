# Imagine que você está desenvolvendo um gerenciador de downloads que permite baixar múltiplos arquivos simultaneamente. Como nem todos os arquivos têm o mesmo tamanho, alguns downloads demoram mais que outros. Seu programa deve:
# Baixar cinco arquivos diferentes, cada um com um tamanho aleatório entre 10MB e 50MB;
# A velocidade de download de cada arquivo é de 5MB por segundo;
# Exibir mensagens de progresso a cada segundo, mostrando quanto já foi baixado de cada arquivo;
# Exibir uma mensagem quando cada download for concluído;
# Aguarde todos os downloads antes de encerrar o programa.

import asyncio
import random

VELOCIDADE_DOWNLOAD = 5 

arquivos = {f'arquivo{i + 1}.txt': random.randint(1,10) * 5 for i in range(5)}

async def monitora_download(nome, tamanho):
    print(f'Iniciando download do {nome} (tamanho: {tamanho})...')
    tempo_execucao = 0
    baixado = 0
    while tamanho > baixado:
        await asyncio.sleep(1)
        tempo_execucao += 1
        baixado += VELOCIDADE_DOWNLOAD
        print(f'[{tempo_execucao}s] {nome}: {baixado}MB baixados')
    print(f'{nome} concluído!')

async def main():
    await asyncio.gather(*(monitora_download(nome, tamanho) for nome, tamanho in arquivos.items()))
    print(f'Todos os downloads foram concluídos!')

asyncio.run(main())

