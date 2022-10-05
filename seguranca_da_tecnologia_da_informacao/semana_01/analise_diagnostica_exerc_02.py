#!/usr/bin/env python3.9



# Crie duas estrutura de dictonario
from uuid import uuid4


materials = {
    uuid4() : 'caderno',
    uuid4() : 'borracha',
    uuid4() : 'tabuada'
}

class Cart:
    def __init__( self ) -> None:
        self.cart: dict[ str, str ] = {}
        self.size: int = 0
        pass

    def add_to_cart( self, item: str ):
        if  item == '':
            print( 'Não é permitido adicionar um itém sem nome.')
        elif not self.max_size():
            self.cart[uuid4()] = item
            self.size += 1
            print( f'Adicionado {item} ao seu carrinho com sucesso' )

    def remove_from_cart( self, key: str ):
        if self.empty():
            del self.cart[key]
            self.size -= 1
        

    def max_size( self ) -> bool:
        if self.size >= 5:
            print( 'Carrinho cheio. Limite máximo de 5 items ocupados.' )
            return True
        return False
    
    def empty( self ) -> bool:
        if self.size <= 0:
            print( 'Não há o que remover nessa lista' )
            return True
        return False

# Imprimeir a lista usando Enumarate
def print_dict( dict: dict[str, str] ):
    id: int = 0
    for key, item in dict.items():
        print( f'[ {id + 1} ]: Chave: {key} - Material: ', item )
        id += 1
    print( '' )



user_cart = Cart()
while True: 
    user_cart.add_to_cart( 'apontador' )
    user_cart.add_to_cart( 'apontador' )
    user_cart.add_to_cart( 'apontador' )
    user_cart.add_to_cart( 'aponta'    )
    user_cart.add_to_cart( 'apontador' )
    user_cart.add_to_cart( 'apontador' )
    user_cart.add_to_cart( '' )


    print_dict(materials)
    print_dict( user_cart.cart )

    break