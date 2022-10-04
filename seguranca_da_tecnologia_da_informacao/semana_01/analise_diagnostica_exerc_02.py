#!/usr/bin/env python3.9

# Crie duas estrutura de dictonario
materials = {
    '0001': 'caderno',
    '0010': 'borracha',
    '0100': 'tabuada'
}

cart: dict[ str, str ] = {}

# Imprimeir a lista usando Enumarate
def print_dict( dict: dict[str, str] ):
    id: int = 0
    for key, item in dict.items():
        print( f'[ {id + 1} ]: Chave: {key}', item )
        id += 1
    print('')

def add_to_cart( item ):
    pass

while True:
    print_dict(materials)

    pass