#!/usr/bin/env python3


import hashlib, subprocess, platform

# ------------------------------------------------------------------------------
# GENERIC 
# Manipulador do terminal
def clear_terminal():
    # Referencia da NET - Danonne
    if platform.system()=="Windows":
        subprocess.Popen("cls",   shell=False).communicate() 
    else: #Linux and Mac
        subprocess.Popen("clear", shell=False).communicate() 


# ------------------------------------------------------------------------------
# __MATERIALS__CLASS__
class Materials:
    def __init__( self ) -> None:
        self.list   : dict[ str, tuple(str, int) ] = {}
        self.size   : int = 0
        self.__limit: int = 10
        self.last : str = ''
        pass

    # Verifica o tamanho limit da lista
    def max_size( self ) -> bool:
        if self.size >= self.__limit:
            print( 'Carrinho cheio. Limite máximo de 5 items ocupados.' )
            return True
        return False

    def collision( self, hash: str ):
        if hash in self.list:
            item, count = self.list[hash]
            print( f'Item {item} já está adicionado nos Materiais')
            print( f'Possuí {count} em estoque')
            return True
        return False

    def add( self, value ):
        hash: str
        if  value == '':
            print( 'Não é permitido adicionar um itém sem nome.')
        elif not self.max_size():
            hash = hashlib.sha256( value.encode('utf8') ).hexdigest()
            if not self.collision( hash ):
                self.list[ hash ] = ( value, 0 )
                print( f'Adicionado {value} ao seu carrinho com sucesso' )
            self.size += 1
            self.last = hash
        return self

    def print_dict( self ):
        id: int = 0
        for key, item in self.list.items():
            print( f'[ {id + 1} ]: Chave: {key[0:5]}...{key[-5:]} - Material: {item[0]} - quantidade: {item[1]}un.' )
            id += 1
        print( '' )

# ------------------------------------------------------------------------------
# __STOCK__CLASS__
class Stock( Materials ):
    def __init__(self) -> None:
        Materials.__init__( self )
        self.buffer: dict[str, tuple[str, int]] = {}

    def __get_last( self ):
        return self.list[self.last]
    
    def __set_last( self, ext_item, ext_num ): 
        self.list[ self.last ] = ( ext_item , ext_num )

    def update_item_number( self, ext_num ):
        item, num = self.__get_last()
        self.__set_last( item , ext_num )

    def add_item_number( self, ext_num ):
        item , num = self.__get_last()
        self.__set_last( item , num + ext_num )

    def sub_item_number( self, ext_num ):
        item , num = self.__get_last()
        self.__set_last( item , num - ext_num )

    def print_dict( self ):
        print('Nossos Materiais em Stock: ')
        Materials.print_dict( self )

    def by_id( self, item: int ):
        count: int = 0
        
        for list_item in self.list.items():
            if count == item:
                self.buffer = list_item
                self.last   = list_item[0]
                return True
            count += 1
        return False
           
    def get_buffer( self ):
        self.sub_item_number(1)
        buffer = self.buffer
        self.buffer = ''
        return buffer


# ------------------------------------------------------------------------------
# __CART_CLASS__
class Cart:
    def __init__( self ) -> None:
        self.cart: dict[ str, tuple(str, int) ] = {}
        self.size: int = 0
        pass

    def add( self, key, value ):
        if  value == '':
            print( 'Não é permitido adicionar um itém sem nome.')
        elif not self.max_size():
            if key in self.cart:
                count: int =  self.cart[key][1] + 1
                self.cart[key] = ( value[0], count )
            else:
                self.cart[ key ] = ( value[0], 1 )
                print( f'Adicionado {value[0]} ao seu carrinho com sucesso' )
            self.size += 1
        self.last = key
        return self

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
    def print_dict( self ):
        id: int = 0
        for key, item in self.cart.items():
            print( f'[ {id + 1} ]: Chave: {key} - Material: {item[0]} - quantidade: {item[1]}un.' )
            id += 1
        print( '' )


# ------------------------------------------------------------------------------
# Funcão para integrar Carrinho com o Estoque na adição de novos itens de compra
def add_to_cart( cart: Cart, stock: Stock ):
    clear_terminal()
    print( 'Escolha até no máximo 5 itens dessa lista para adicionar em seu carrinho.')
    print( 'Quando quiser encerrar precione zero.')
    stock.print_dict()
    while True: 
        txt_opt: str = input( 'opção: ' )

        try:
            num_opt = int( txt_opt )

            if num_opt <= 0:
                print( 'Espero que tenha adorado a experiência' )
                break

            if num_opt <= stock.size:
                if cart.max_size():
                    print('Sua lista de compras está cheia')
                elif stock.by_id(num_opt - 1):
                    key, value = stock.get_buffer()
                    cart.add( key, value )

                    clear_terminal()
                    print( 'Quando quiser encerrar precione zero.')
                    stock.print_dict()
                    cart.print_dict()
                continue

            print( 'São aceitos apenas valores existentes na lista' )

        except ValueError:
            print( 'Desculpe, mas serão aceitos apenas números inteiro' )



# ------------------------------------------------------------------------------
# Iniciando parte estática da aplicação
user_cart: Cart = Cart()
stock: Stock= Stock()
stock.add( 'lapiz'     ).add_item_number(5)
stock.add( 'postit'    ).add_item_number(5)
stock.add( 'caneta'    ).add_item_number(5)
stock.add( 'caderno'   ).add_item_number(5)
stock.add( 'corretiv'  ).add_item_number(5)
stock.add( 'borracha'  ).add_item_number(5)
stock.add( 'canetinha' ).add_item_number(5)
stock.add( 'apontador' ).add_item_number(5)

# ------------------------------------------------------------------------------
# Inicando parte dinâmica da aplicação
clear_terminal()
while True:
    print( 'Seja bem vindo(a) a nossa loja de materiais escolares. Precione o número referente ao opção desejada.' )
    print( '1 - Adicionar no Carrinho de Comprar' )
    print( '2 - Remover do Carrinho de Comprar'   )
    print( '3 - Visualizar minha lista completa'  )
    print( 'Precione Qualquer Tecla para Encerrar o Programa' )

    match input( 'opção: ' ):
        case '1':
            clear_terminal()
            add_to_cart( user_cart, stock )
        case '2':
            print('2')
        case '3':
            clear_terminal()
            user_cart.print_dict()
        case _:
            del user_cart
            del stock
            break

