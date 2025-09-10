# Curso: Avançando na Orientação a Objetos e Consumindo API

## Descrição
Neste curso aprofundamos os conhecimentos em **Programação Orientada a Objetos (POO)**, explorando herança, polimorfismo e abstração.  
Também aprendemos a criar e gerenciar **ambientes virtuais**, consumir dados externos via **API** com o módulo `requests`, manipular arquivos JSON e criar nossa própria API utilizando o **FastAPI**.

## Conteúdos Abordados
- Criação da classe principal `ItemCardapio` com atributos `nome` e `preço`.
- Implementação das classes `Bebida` e `Prato`, herdando da classe `ItemCardapio` com uso de `super()`.
- Instanciação de objetos de `Prato` e `Bebida`, demonstrando a reutilização de funcionalidades via herança.
- Criação de método para adicionar itens ao cardápio, aceitando qualquer instância de `ItemCardapio`.
- Uso de `property` para exibir o cardápio de cada restaurante.
- Implementação de método abstrato `aplicar_desconto`, aplicado em pratos e bebidas.
- Demonstração de **polimorfismo**, onde diferentes classes respondem ao mesmo método de formas distintas.
- Criação e ativação de ambientes virtuais com **venv**.
- Documentação e gerenciamento de dependências com `requirements.txt`.
- Requisições a uma **API de restaurantes** utilizando o módulo `requests`.
- Armazenamento e manipulação de dados em arquivos JSON.
- Criação de uma API com **FastAPI**.
- Desenvolvimento de endpoints para listar e filtrar restaurantes por nome.
- Exploração das documentações interativas **docs** e **redoc** do FastAPI.

## Projeto Desenvolvido
O projeto final consistiu em um sistema de restaurantes que permitiu:
- Gerenciar um cardápio com itens de diferentes tipos (pratos e bebidas).
- Aplicar descontos específicos em itens, reforçando conceitos de herança e polimorfismo.
- Consumir dados de uma API externa de restaurantes e salvar as informações em arquivos JSON.
- Criar e disponibilizar uma API própria utilizando o FastAPI, com endpoints para consulta e filtragem de restaurantes.
- Gerenciar dependências em um ambiente virtual isolado.

### Estrutura de Arquivos
- `hora_da_praticaXX.py`: exercícios práticos desenvolvidos ao longo das aulas.  
- `item_cardapio.py`: definição da classe base **ItemCardapio**.  
- `prato.py`: definição da classe **Prato**.  
- `bebida.py`: definição da classe **Bebida**.  
- `restaurante.py`: definição da classe **Restaurante**.  
- `avaliacao.py`: definição da classe **Avaliação**.  
- `app.py` (em `oo_sabor_express`): código principal do sistema de restaurantes.  
- `app.py` (em `oo_sabor_express_api`): consumo da API externa de restaurantes e geração de arquivos JSON individuais para cada restaurante.  
- `main.py`: execução do servidor FastAPI.  
- `requirements.txt`: dependências do projeto.

## Aprendizados Principais
- Aplicação de conceitos avançados de POO: herança, abstração, polimorfismo e métodos especiais.
- Uso de `super()` para aproveitar e estender funcionalidades da classe pai.
- Boas práticas com ambientes virtuais e documentação de dependências.
- Consumo e manipulação de dados externos via API com o módulo `requests`.
- Criação e uso de arquivos JSON para persistência de dados.
- Desenvolvimento de uma API completa com o **FastAPI**, incluindo documentação interativa.
