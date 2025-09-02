# Curso: Aplicando Orientação a Objetos em Python

## Descrição
Neste curso exploramos os fundamentos da **Programação Orientada a Objetos (POO)** em Python, entendendo a importância das classes como estrutura central para organizar e modularizar o código.  
Construímos nossa primeira classe, **Restaurante**, e avançamos gradualmente até integrar múltiplas classes, como **Restaurante** e **Avaliação**, consolidando os princípios essenciais da POO.

## Conteúdos Abordados
- Introdução ao conceito de **classe** no paradigma de Orientação a Objetos.
- Criação da classe `Restaurante` com atributos de instância (`nome`, `categoria` e `ativo`).
- Utilização do método construtor `__init__` para inicializar atributos, incluindo o estado padrão de `ativo = False`.
- Diferença entre **atributos de classe** e **atributos de instância**.
- Uso de **underscore (`_`)** para indicar atributos protegidos.
- Aplicação da função `property` em atributos (`categoria` e `ativo`) para controle e abstração.
- Criação e uso de **métodos de classe**, como `listar_restaurantes`.
- Prática de **abstração**, representando o estado ativo/inativo de forma visual.
- Importação de classes entre arquivos (`main.py` e módulos auxiliares).
- Criação de novas classes para reforçar os fundamentos da POO.
- Integração entre classes: associação entre `Restaurante` e `Avaliação`.
- Gerenciamento e listagem de objetos de avaliação associados a cada restaurante.

## Projeto Desenvolvido
O projeto principal consistiu em um sistema de restaurantes que permitiu:
- Criar e gerenciar restaurantes com atributos específicos.
- Listar os restaurantes existentes e exibir seu estado (ativo/inativo).
- Importar classes em diferentes módulos e utilizar suas funcionalidades.
- Criar e associar avaliações aos restaurantes, exibindo todas as avaliações vinculadas.

### Estrutura de Arquivos
- `main.py`: arquivo principal, responsável pela execução do programa.
- `restaurante.py`: definição da classe **Restaurante**.
- `avaliacao.py`: definição da classe **Avaliação**.
- `hora_da_praticaXX.py`: exercícios práticos realizados ao longo do curso.

## Aprendizados Principais
- Importância das classes para modularização e reutilização de código.
- Diferença e uso correto de atributos de instância e de classe.
- Controle de acesso a atributos com **underscore** e **property**.
- Criação e uso de métodos especiais (`__init__`) e métodos de classe.
- Integração entre diferentes classes, reforçando os conceitos de **abstração** e **associação**.
- Capacidade de construir programas mais robustos e organizados utilizando os princípios da Programação Orientada a Objetos.