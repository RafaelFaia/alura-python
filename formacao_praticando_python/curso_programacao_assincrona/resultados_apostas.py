# Você foi contratado para desenvolver um sistema de apostas esportivas assíncrono. Os jogadores fazem suas apostas em jogos de futebol, mas os resultados só são revelados depois de um tempo aleatório, simulando a espera real por um resultado.
# Nesta tarefa, você deve:
# Criar um sistema onde cada aposta é armazenada em um asyncio.Future() e só é definida após um tempo determinado;
# Simular três jogos diferentes, nos quais os apostadores fizeram suas apostas;
# O resultado de cada jogo será "Vitória do Time A", "Vitória do Time B" ou "Empate", escolhido aleatoriamente;
# Cada jogo levará entre 2 e 8 segundos para ter seu resultado definido;
# O programa não deve esperar cada aposta individualmente, ele deve registrar todas e continuar rodando;
# Assim que um resultado for definido, ele deve ser exibido imediatamente;
# Quando todos os jogos forem finalizados, o programa exibe a mensagem "Todos os resultados foram revelados!".
# Variáveis pré-definidas:
# jogos = [
#     {"id": 1, "times": "Flamengo vs Palmeiras"},
#     {"id": 2, "times": "São Paulo vs Corinthians"},
#     {"id": 3, "times": "Grêmio vs Internacional"},
# ]
# RESULTADOS = ["Vitória do Time A", "Vitória do Time B", "Empate"]

import asyncio
import random

jogos = [
    {"id": 1, "times": "Flamengo vs Palmeiras"},
    {"id": 2, "times": "São Paulo vs Corinthians"},
    {"id": 3, "times": "Grêmio vs Internacional"},
]

RESULTADOS = ["Vitória do Time A", "Vitória do Time B", "Empate"]

async def processar_aposta(jogo, future):
    tempo_espera = random.randint(2, 8)
    await asyncio.sleep(tempo_espera)
    resultado = random.choice(RESULTADOS)
    future.set_result((jogo, resultado, tempo_espera))

async def revelar_resultado(future):
    jogo, resultado, tempo = await future # não utiliza futuro.result() pois o result ainda não está pronto, tem que aguardar ele (await)
    time_a, time_b = jogo["times"].split(" vs ")
    if resultado == "Vitória do Time A":
        resultado_formatado = f"Vitória do {time_a}"
    elif resultado == "Vitória do Time B":
        resultado_formatado = f"Vitória do {time_b}"
    else:
        resultado_formatado = "Empate"
    print(f"Aposta no jogo {jogo['id']} definida: {resultado_formatado} (após {tempo}s).")

async def main():
    futures = []
    
    for jogo in jogos:
        future = asyncio.Future()
        futures.append(future)
        print(f"Aposta no jogo {jogo['id']} ({jogo['times']}) registrada! Aguardando resultado...")
        asyncio.create_task(processar_aposta(jogo, future))

    await asyncio.gather(*(revelar_resultado(f) for f in futures))
    print("\nTodos os resultados foram revelados!")

asyncio.run(main())

# Outro método de se resolver, porém mais complexo:
# import asyncio
# import random

# jogos = [
#     {"id": 1, "times": "Flamengo vs Palmeiras"},
#     {"id": 2, "times": "São Paulo vs Corinthians"},
#     {"id": 3, "times": "Grêmio vs Internacional"},
# ]
# RESULTADOS = ["Vitória do Time A", "Vitória do Time B", "Empate"]

# async def processar_aposta(jogo, futuro):
#     tempo = random.randint(2, 8)
#     await asyncio.sleep(tempo)
    
#     times = jogo["times"].split(" vs ")
#     resultado_bruto = random.choice(RESULTADOS)
    
#     if resultado_bruto == "Vitória do Time A":
#         resultado = f"Vitória do {times[0]}"
#     elif resultado_bruto == "Vitória do Time B":
#         resultado = f"Vitória do {times[1]}"
#     else:
#         resultado = "Empate"
    
#     futuro.set_result((resultado, tempo))

# def quando_resultado_pronto(jogo, futuro):
#     resultado, tempo = futuro.result() #usa futuro.result() pois o result obrigatóriamente estará pronto a essa altura, por conta do callback
#     print(f"Aposta no jogo {jogo['id']} definida: {resultado} (após {tempo}s).")

# async def main():
#     futuros = []
    
#     for jogo in jogos:
#         futuro = asyncio.Future()
#         futuro.add_done_callback(lambda f, j=jogo: quando_resultado_pronto(j, f))
#         futuros.append(futuro)
        
#         asyncio.create_task(processar_aposta(jogo, futuro))
#         print(f"Aposta no jogo {jogo['id']} ({jogo['times']}) registrada! Aguardando resultado...")
    
#     await asyncio.gather(*futuros)
#     print("\nTodos os resultados foram revelados!")

# asyncio.run(main())