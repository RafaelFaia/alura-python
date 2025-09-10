from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('Praça', 'Gourmet')
suco_melancia = Bebida('Suco de Melancia', 5.00, 'Grande')
suco_melancia.aplicar_desconto()
pao = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
pao.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(suco_melancia)
restaurante_praca.adicionar_no_cardapio(pao)

# restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

# restaurante_praca.receber_avaliacao('Rafael', 3)
# restaurante_praca.receber_avaliacao('Laís', 5)

# restaurante_praca.alterar_estado()
# print(restaurante_pizza.ativo)
# Restaurante.listar_restaurantes()

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()