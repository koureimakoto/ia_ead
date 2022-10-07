#!/usr/bin/env python3.9


# GENERIC
# Manipulador do terminal
import platform
import subprocess


def clear_terminal():
    # Referencia da NET - Danonne
    if platform.system()=="Windows":
        subprocess.Popen("cls",   shell=False).communicate() 
    else: #Linux and Mac
        subprocess.Popen("clear", shell=False).communicate() 



# Crie duas estrutura de dictonario
from uuid import uuid4


materials = {
    uuid4() : 'caderno',
    uuid4() : 'borracha',
    uuid4() : 'tabuada'
}

class Cart:
    def __init__( self ) -> None:
        self.cart: dict[ str, tuple(str, int) ] = {}
        self.size: int = 0
        pass

    def add_to_cart( self, key, value ):
        if  value == '':
            print( 'Não é permitido adicionar um itém sem nome.')
        elif not self.max_size():
            if key in self.cart:
                count: int =  self.cart[key][1] + 1
                self.cart[ key] = (value, count ) 
            else:
                self.cart[ key ] = ( value, 1 )
                print( f'Adicionado {value} ao seu carrinho com sucesso' )
            self.size += 1

    def list_to_cart( self, item: int ):
        count: int = 0
        for key, value in materials.items():
            if count == item:
                self.add_to_cart( key, value )
            count += 1

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
        print( f'[ {id + 1} ]: Chave: {key} - Material: {item[0]} - quantidade: {item[1]}un.' )
        id += 1
    print( '' )



user_cart = Cart()
print( 'Escolha até no máximo 5 itens dessa lista para adicionar em seu carrinho.')
print( 'Quando quiser encerrar precione zero.')
while True: 
    txt_opt: str = input( 'opção: ' )

    try:
        num_opt = int( txt_opt )

        if num_opt <= 0:
            print( 'Espero que tenha adorado a experiência' )
            break

        if num_opt <= len( materials ):
            user_cart.list_to_cart( num_opt - 1 )
            continue
        print( 'São aceitos apenas valores existentes na lista' )

    except ValueError:
        print( 'Desculpe, mas serão aceitos apenas números inteiro' )

print_dict( user_cart.cart )