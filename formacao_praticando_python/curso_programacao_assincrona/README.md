# Curso: Praticando Python – Programação Assíncrona

## Descrição
Neste curso, exploramos a **programação assíncrona em Python** utilizando o módulo `asyncio`.  
Aprendemos a lidar com tarefas que possuem tempos de execução variáveis, executando múltiplas operações em paralelo de maneira eficiente.  
Foram praticados conceitos fundamentais de concorrência, sincronização e coordenação de tarefas assíncronas no Python moderno.

## Conteúdos Abordados
- Criação de **corrotinas assíncronas** com `async def` e uso de `await`.  
- Simulação de tempos de espera com `asyncio.sleep()`.  
- Execução de múltiplas tarefas em paralelo com `asyncio.gather()`, `asyncio.create_task()` e `asyncio.Future()`.  
- Utilização de `asyncio.run()` para inicializar e gerenciar o loop de eventos principal.  
- Controle de concorrência com **locks** (`asyncio.Lock()`) e **semáforos** (`asyncio.Semaphore()`).  
- Manipulação de callbacks com `add_done_callback()` para tratar resultados assim que tarefas são concluídas.  

## Projeto Desenvolvido
O projeto consistiu em pequenos programas que aplicaram conceitos de programação assíncrona para simular cenários reais, como monitoramento de downloads, execução de múltiplas tarefas em paralelo, notificações inteligentes e processamento de pedidos em lojas online.

## Estrutura de Arquivos
- `executando_tarefas_simultaneamente.py`: execução de múltiplas tarefas ao mesmo tempo.  
- `fatorial_assincrono_paralelo.py`: cálculo de fatoriais de forma assíncrona em paralelo.  
- `gerenciando_inscricoes_cursos.py`: gerenciamento de inscrições em cursos com tarefas assíncronas.  
- `monitoramento_download.py`: simulação de monitoramento de downloads.  
- `monitorando_tarefas.py`: acompanhamento de tarefas com `asyncio.create_task()`.  
- `processando_pedidos_loja.py`: processamento assíncrono de pedidos em uma loja.  
- `resultados_apostas.py`: sistema de apostas com resultados definidos de forma assíncrona.  
- `simulacao_sensores.py`: simulação de sensores rodando em paralelo.  
- `sistema_notificacao_inteligente.py`: notificações inteligentes disparadas de forma assíncrona.  
- `temporizador_assincrono.py`: implementação de um temporizador com `asyncio`.  

## Aprendizados Principais
- Criação e execução de corrotinas assíncronas com `async def` e `await`.  
- Coordenação de múltiplas tarefas em paralelo usando `asyncio`.  
- Controle de concorrência com locks e semáforos.  
- Integração de callbacks para processamento imediato de resultados.  
- Aplicação de programação assíncrona em cenários práticos como monitoramento, notificações e processamento de dados.  