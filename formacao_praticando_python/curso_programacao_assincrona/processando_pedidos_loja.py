# Marcos é dono de uma loja online e precisa de um sistema que processe pedidos de forma assíncrona. O sistema deve seguir a seguinte lógica:
# Primeiro, verificar se o pagamento foi aprovado;
# Se o pagamento for aprovado, verificar se há estoque disponível;
# Somente se houver estoque disponível, confirmar o pedido e enviá-lo para entrega;
# Se o pagamento falhar ou não houver estoque, o pedido deve ser cancelado.
# A lista de pedidos já está definida no sistema, com o status do pagamento e do estoque previamente cadastrados. Confira o código:
# pedidos = [
#     {'id': 101, 'pagamento_aprovado': True, 'estoque_disponivel': True},
#     {'id': 102, 'pagamento_aprovado': True, 'estoque_disponivel': False},
#     {'id': 103, 'pagamento_aprovado': False, 'estoque_disponivel': True},
#     {'id': 104, 'pagamento_aprovado': True, 'estoque_disponivel': True},
#     {'id': 105, 'pagamento_aprovado': False, 'estoque_disponivel': False},
# ]
# O programa deve simular essa lógica para três pedidos, exibindo mensagens conforme o processamento ocorre.

import asyncio

pedidos = [
    {'id': 101, 'pagamento_aprovado': True, 'estoque_disponivel': True},
    {'id': 102, 'pagamento_aprovado': True, 'estoque_disponivel': False},
    {'id': 103, 'pagamento_aprovado': False, 'estoque_disponivel': True},
    {'id': 104, 'pagamento_aprovado': True, 'estoque_disponivel': True},
    {'id': 105, 'pagamento_aprovado': False, 'estoque_disponivel': False},
]

async def verificar_pagamento(pedido):
    await asyncio.sleep(1)
    if pedido['pagamento_aprovado']:
        print(f'Pagamento aprovado para pedido #{pedido["id"]}.')
        return True
    else:
        print(f'Pagamento recusado para pedido #{pedido["id"]}. Pedido cancelado.')
        return False

async def verificar_estoque(pedido):
    await asyncio.sleep(1)
    if pedido['estoque_disponivel']:
        print(f'Estoque disponível para pedido #{pedido["id"]}.')
        return True
    else:
        print(f'Estoque indisponível para pedido #{pedido["id"]}. Pedido cancelado.')
        return False

async def processar_pedido(pedido, semaphore):
    async with semaphore:
        print(f'\nProcessando pedido #{pedido["id"]}...')
        
        if not await verificar_pagamento(pedido):
            return
        if not await verificar_estoque(pedido):
            return
        print(f'Pedido #{pedido["id"]} confirmado! Enviado para entrega.')

async def main():
    semaphore = asyncio.Semaphore(3)
    tarefas = [asyncio.create_task(processar_pedido(pedido,semaphore)) for pedido in pedidos]
    await asyncio.gather(*tarefas)
    print('\nTodos os pedidos foram processados!\n')

asyncio.run(main())