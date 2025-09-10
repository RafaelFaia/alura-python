# 1 - Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

# 2 - No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self,marca, modelo):
        self._marca = marca
        self._modelo = modelo
        
    @abstractmethod
    def ligar(self):
        pass

# 3 - Crie uma nova classe chamada Carro que herda da classe Veiculo.
# from veiculo import Veiculo

class Carro(Veiculo):

    def ligar(self):
        pass

# 4 - No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
# from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor

    def ligar(self):
        pass

# 5 - Em um arquivo chamado main.py, importe a classe Carro.
# from carro import Carro

# 6 - No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.
# from carro import Carro

carro1 = Carro(marca="Ford", modelo="Focus", cor="Preto")
carro2 = Carro(marca="Chevrolet", modelo="Cruze", cor="Prata")
carro3 = Carro(marca="Honda", modelo="Civic", cor="Vermelho")