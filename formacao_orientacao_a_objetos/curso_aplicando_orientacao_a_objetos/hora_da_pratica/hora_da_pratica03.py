# 1 - Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

# 2 - Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
    
    def __str__(self):
        return f'Conta de {self.titular} - Saldo: R${self.saldo}'
    
conta1 = ContaBancaria('Rafael Faia', 1000)
conta2 = ContaBancaria('Laís Valente', 2000)

# 3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False
    
    def __str__(self):
        return f'Conta de {self.titular} - Saldo: R${self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True
    
conta3 = ContaBancaria('Rafael Faia', 500)
ContaBancaria.ativar_conta(conta3)
print(conta3.ativo)


# 4 - Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Conta de {self._titular} - Saldo: R${self._saldo}'
    
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    def ativar_conta(self):
        self._ativo = True

# 5 - Crie uma instância da classe e imprima o valor da propriedade titular.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Conta de {self._titular} - Saldo: R${self._saldo}'
    
    @property
    def titular(self):
        return self._titular

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'
    
    def ativar_conta(self):
        self._ativo = True

conta4 = ContaBancaria('Rafael Faia', 10)
print(conta4.titular)

# 6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
        self._profissao = profissao

cliente1 = ClienteBanco("Ana", 30, "Rua A", "123.456.789-01", "Backend")
cliente2 = ClienteBanco("Luiza", 25, "Rua B", "987.654.321-01", "Estudante")
cliente3 = ClienteBanco("Vinny Neves", 40, "Rua C", "111.222.333-44", "Frontend")

# 7 - Crie um método de classe para a conta ClienteBanco.
class ClienteBanco:
    clientes = []

    def __init__(self, nome, idade, endereco, cpf, profissao):
        self._nome = nome
        self._idade = idade
        self._endereco = endereco
        self._cpf = cpf
        self._profissao = profissao
        ClienteBanco.clientes.append(self)

    @classmethod
    def listar_clientes(cls):
        for cliente in cls.clientes:
            print(f"{cliente._nome} - {cliente._profissao}")

ClienteBanco.listar_clientes()

