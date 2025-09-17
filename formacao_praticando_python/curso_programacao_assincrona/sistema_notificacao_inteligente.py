# Lucas trabalha em um sistema de notificações que precisa enviar mensagens para usuários. No entanto, algumas notificações só devem ser enviadas se o usuário tiver ativado essa opção no sistema. Além disso, se o usuário for VIP, ele deve receber uma notificação prioritária antes das demais.
# Com base nesse cenário, crie um programa que simule o envio de notificações para três usuários. Cada usuário tem um status diferente:
# Ana: VIP (deve receber uma notificação prioritária antes das normais).
# João: Usuário comum, mas ativou as notificações.
# Carla: Usuária comum, mas desativou as notificações (não deve receber nada).
# O programa deve exibir quais notificações foram enviadas e quais usuários não receberam nada.

import asyncio

usuarios = [
    {'nome': 'Carla', 'vip': False, 'notificacoes_ativadas': False},
    {'nome': 'João', 'vip': False, 'notificacoes_ativadas': True},
    {'nome': 'Ana', 'vip': True, 'notificacoes_ativadas': True}
]

async def enviar_notificacoes(usuario):
    if not usuario['notificacoes_ativadas']:
        await asyncio.sleep(2)
        print(f'{usuario['nome']} desativou as notificações. Nada foi enviado.')
        return
    
    if not usuario['vip']:
        await asyncio.sleep(1)
        print(f'Notificação normal para {usuario['nome']} enviada!')
        return
    
    print(f'Notificação VIP para {usuario['nome']} enviada!')

async def main():
    tarefas = [asyncio.create_task(enviar_notificacoes(usuario)) for usuario in usuarios]
    await asyncio.gather(*tarefas)
    print('Todas as notificações foram processadas!')

asyncio.run(main())
