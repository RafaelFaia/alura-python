from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
# restaurante_pizza = Restaurante('Pizza Express', 'Italiana')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

restaurante_praca.receber_avaliacao('Rafael', 8)
restaurante_praca.receber_avaliacao('Laís', 10)

# restaurante_praca.alterar_estado()
# print(restaurante_pizza.ativo)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()