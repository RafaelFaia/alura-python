# 1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

meu_carro = Carro('Tiggo 7', 'Chumbo', '2025')

# 2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
class Restaurante:
    def __init__(self, nome, categoria, capacidade, nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

meu_restaurante = Restaurante('Restaurante do Rafa', 'Churrascaria', 100, 5)

# 3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

novo_restaurante = Restaurante(nome='Restaurante da Laís', categoria='Sushi Lounge')

# 4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
class Restaurante:
    def __init__(self, nome, categoria, capacidade=0, nota_avaliacao=0.0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
mais_um_restaurante = Restaurante('Bar do Jura', 'Bar')
print(mais_um_restaurante)

# 5 - Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

cliente1 = Cliente('Rafael', 26, 'RafaelFaiaC@gmail.com', '(13)98121-4046')
cliente2 = Cliente('Laís', 25, 'lais.v299@gmail.com', '(13)99634-4020')
cliente3 = Cliente('Jurandir', 55, 'Jurandir.Jr70@gmail.com', '(13)98121-5415')