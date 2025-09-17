# Lucas está desenvolvendo um sistema de monitoramento ambiental. Para isso, ele precisa criar sensores assíncronos que coletam dados periodicamente, sem que o programa fique travado esperando por cada um.
# O sistema deve ter três sensores, que coletam e exibem dados em intervalos diferentes:
# Sensor de temperatura: Atualiza os dados a cada 2 segundos.
# Sensor de umidade: Atualiza os dados a cada 3 segundos.
# Sensor de qualidade do ar: Atualiza os dados a cada 5 segundos.
# O sistema nunca deve parar de rodar, exibindo os valores atualizados de cada sensor assim que novos dados estiverem disponíveis.
# Dica: Utilize uma corrotinas para resolver este problema e use o método random.choice para definir a temperatura e qualidade do ar.

import asyncio
import random

async def sensor_temperatura():
    tempo_execucao = 2
    while True:
        await asyncio.sleep(2)
        print(f'[{tempo_execucao}s] Temperatura: {random.randint(20,30)}°C')
        tempo_execucao += 2
    
async def sensor_umidade():
    tempo_execucao = 3
    while True:
        await asyncio.sleep(3)
        print(f'[{tempo_execucao}s] Umidade: {random.randint(50,70)}%')
        tempo_execucao += 3

async def sensor_qualidade_ar():
    tempo_execucao = 5
    while True:
        await asyncio.sleep(5)
        print(f'[{tempo_execucao}s] Qualidade do ar: {random.choice(['Boa','Regular','Ruim'])}')
        tempo_execucao += 5

async def main():
    await asyncio.gather(
        sensor_temperatura(),
        sensor_umidade(),
        sensor_qualidade_ar()
    )

asyncio.run(main())