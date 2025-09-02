# 1 - Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

# 2 - Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'Livro: {self._titulo} | Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao}'

livro1 = Livro('O Milagre da Manhã', 'Hal Elrod', 2012)
livro2 = Livro('O Poder do Hábito', 'Charles Duhigg', 2012)

print(livro1)
print(livro2)

# 3 - Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'Livro: {self._titulo} | Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao}'
    
    def emprestar(self):
        self._disponivel = False

    @property
    def disponivel(self):
        return 'Disponível' if self._disponivel else 'Indisponível'

livro3 = Livro('Por que nós dormimos: A nova ciência do sono e do sonho', 'Matthew Walker', 2018)
livro3.emprestar()
print(livro3.disponivel)

# 4 - Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'Livro: {self._titulo} | Autor: {self._autor} | Ano de Publicação: {self._ano_publicacao}'
    
    def emprestar(self):
        self._disponivel = False

    @property
    def disponivel(self):
        return 'Disponível' if self._disponivel else 'Indisponível'
    
    @staticmethod #apesar de @classmethod fazer mais sentido
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro._titulo for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis

# 5 - Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
#Arquivo biblioteca.py:
#from livro import Livro
#Observação: deixando comentado para não ficar com mensagem de erro.

# 6 - No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro3 = Livro('Hábitos Atômicos', 'James Clear', 2018)
livro3.emprestar()
print(livro3.disponivel)

# 7 - No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
livros_disponiveis = Livro.verificar_disponibilidade(2018)

# 8 - Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
#Arquivo biblioteca.py:
#from livro import Livro
#Observação: deixando comentado para não ficar com mensagem de erro.

livro1 = Livro('O Milagre da Manhã', 'Hal Elrod', 2012)
livro2 = Livro('O Poder do Hábito', 'Charles Duhigg', 2012)

print(livro1)
print(livro2)