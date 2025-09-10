from modelos.avaliacao import Avaliacao 
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 1 <= nota <= 5:
            self._avaliacao.append(Avaliacao(cliente, nota))

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliações'
        return round((sum(avaliacao._nota for avaliacao in self._avaliacao)) / len(self._avaliacao), 1)

    def adicionar_no_cardapio(self, item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)
    
    @property            
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante: {self._nome}\n')
        for i, item in enumerate(self._cardapio, 1): 
            if hasattr(item, '_descricao'):
                print(f'{i}. Nome: {item._nome} | Preço {item._preco} | Descricao: {item._descricao}')
            if hasattr(item, '_tamanho'):
                print(f'{i}. Nome: {item._nome} | Preço {item._preco} | Tamanho: {item._tamanho}')
