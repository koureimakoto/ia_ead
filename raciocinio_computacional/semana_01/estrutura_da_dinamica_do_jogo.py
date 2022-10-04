#!/usr/bin/env python3.9

# __ FUNCTIONS __

"""
This function return a option greater than 0 and process only literal number

get_option:
    >> msg: str | msg: str = 'opção: '
    >> min: int | min: int = 0
    << option: int
"""
def get_input_number( msg: str = 'opção: ', min: int = 0) -> int:
    while True:
        try:
            option = int( input( msg) )
            if option > min:
                return option
            print( 'Digite números maiores zero' )
        except ValueError:
            print( 'Digite apenas números inteiros' )

"""
This function return a player name list 

get_player_name:
    >> player_number: int | player_number: int = 0
    << player_names : list
"""
def get_player_name( player_number: int = 0 ):
    if player_number <= 0:
        print( 'Desculpe, aconteceu algum erro com a quantidade de jogadores.' )

    print( 'Preciso que você me informe o nome do jogador' )

    count       : int  = 0
    player_names: list = []
    while True:
        buff: str = input( 'Digite o nome: ' )
        if buff == '':
            print( 'Nomes vazios não serão aceitos' )
            continue

        player_names.append( buff )
        print( f'Jogador [{buff}] adiconado com sucesso' )
        
        count += 1
        if count >= player_number:
            print( 'Pronto, adicionamos todos' )
            return player_names
        print( 'Vamos para o próximo' )
    pass

print( 'Vamos iniciar de forma simples! Me indique quantos jogadores teremos?' )
option      : int  = get_input_number( 'quantidade: ' )
player_names: list = get_player_name( option )


