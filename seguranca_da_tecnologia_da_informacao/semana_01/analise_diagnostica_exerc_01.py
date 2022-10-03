#!/usr/bin/env python3

"""
 Nota 
 
 O exagero no código é por motivo de teste. Tipo manuseio de python e gostaria de testar
 algumas funcionalidades como try e arquivo.


 Talles H.
"""


# Funcoes
from io import TextIOWrapper


# Imprimeir a lista usando Enumarate
def print_list( list: list ):
    list_size = len(list)
    for i, item in enumerate(list):
        print( f'[ {i + 1} ]: ', item )
    print('')

def add_to_user_favorites( item ):
    favorites.append(item)
    print( f'{item} adicionado com sucesso')

def protect_me( file_descriptor, file_buffer ):
    if file_buffer != '':
        if file_buffer[ 0 ] == '1':
            count: int = int( file_descriptor.readline() ) + 1
            file_descriptor.seek( 2 )
            file_descriptor.write( f'{count}\n' )
            file_descriptor.close()

                # Se tentar mais de uma, enviar mensagem
            if count >= 1:
                print( 'Não adianta insistir baby' )
                print( f'Já tentou {count}x, não seria melhor descobrir o por quê? Será mais divertido')
        exit()

def init_openning_option():
    print('Escolha uma das opções e pressione ENTER para efetivar')
    print( '1 - Ver lista' )
    print( '2 - Adicionar manualmente' )
    print( '3 - Ver meus favoritos' )
    print( 'OU qualquer tecla para sair')

    return input( 'opção: ')

# Crie uma lista vazia em Python
# Variaveis Globais
movies   : list = [
    'Guerreiros da Galáxia',
    'Um Ome Morcego',
    'O Verde dos Nataiz',
    'Morbido e sua mulher abusiva', 
    'Criatividade se foi no quinto'
]

favorites: list = []



# Ficou brincando ne? Ta lendo agora aqui para saber como voltar a funcionar?
FILE: TextIOWrapper
FILE_NAME  : str = '.byeignore'
FILE_BUFFER: str = ''
try:
    FILE = open( FILE_NAME, 'r+')
    FILE_BUFFER = FILE.readline()
    protect_me( FILE, FILE_BUFFER )
except FileNotFoundError:
    FILE = open( FILE_NAME, 'w')
    FILE.close()

# Adicione o nome de 5 filmes da lista de favoritos
print( 'Seja bem vindo a ao NetList, seu catalogo interativo' )
print( 'Selecione os filmes listados ou, caso preferir você poderá adicionar manualmente.' )

while True:
    option:str = init_openning_option()
    match option:
        case '1': 

            # Exibe menu
            print_list(movies)
            print( 'Lista top, não?, quer escolher algum eu deseja retornar ao menu inicial?')
            print( 'Caso queira sair, escolha 0 (zero) para retornar ao menu inicial')
            
            while True: 
                # Recebe um optacao supostamente numerica
                int_option: str = input('opção: ')
                
                # Verifica se o usuario quer sair, se nao vai cair na excessao
                if int_option == '0':
                    break

                # Caso o valor digita nao seja um numero inteiro evoca um erro
                try:
                    id = int(int_option)
                    add_to_user_favorites( movies[id - 1] )
                    print_list( favorites )
                except ValueError:
                    print( 'Desculpe, mas digite apenas números inteiros.' )

        case '2':
            
            print( 'Olha, não sou o mestre do português, mas tenta não escreve muinto errado.' )
            print( 'Se desistir só digitar 0 (zero) que devolvo para o menu incial')
            
            adicional_msg = ''
            erro_count: int = 0
            while True:
                manual_movie_title: str = input( f' {adicional_msg} --> ' )

                # Retorna ao menu inicial marotamente
                if manual_movie_title == '0':
                    break

                # Maquina bolada
                if manual_movie_title == '':
                    if   erro_count > 3:
                        # Settar Variavel de Amabiente, sem ela o software da exit
                        FILE = open( FILE_NAME, 'w' )
                        FILE.write('1\n0\n')
                        FILE.close()
                        print( 'Te avise agora SE VIRÁ' )
                        exit()
                    elif erro_count == 3:
                        print( 'Ta de sacanagem né? a próxima vez te tiro desse programa que você não vai conseguir executar mais' )
                        adicional_msg = 'AQUI Ó >>>> '
                    elif erro_count == 2:
                        print( '... Vou te ensinar ta, pode ser que ainda esteja aprendendo a usar o teclado')
                        adicional_msg = 'Aperte os teclas no \'teclado\' onde tem letrinhas'
                    elif erro_count == 1:
                        print( 'Não achou que da segunda vez iria passar não é mesmo?')
                    else:
                        print( 'Maooei, alguém aqui não digitou nada, achou que ia passar? tente novamente por gentileza' )

                    erro_count += 1
                    continue

                print( 'Espero que seja um bom filme para a ir a lista, nao quero ter programado isso atoa em!' )
                add_to_user_favorites( manual_movie_title )
                print_list(favorites)

                print( 'Quer adicionar mais algum titulo manualmente? Se sim só digitar o titulo, se não digite aquele 0 (zero) maroto' )
        case '3':
            print( 'Eh pra já:')
            print_list( favorites )
        case _:
            print('passou')

    