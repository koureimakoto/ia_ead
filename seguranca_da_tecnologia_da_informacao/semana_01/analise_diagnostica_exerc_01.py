#!/usr/bin/env python3

"""
Nota 

O exagero no código é por motivo de teste. Tipo manuseio de python e gostaria de testar
algumas funcionalidades como try e arquivo.

Talles H.
"""

"""
Este código é um referente ao exercicio de Análise Diagnóstica 01
realizado pelo Alunos Talles H. do curso de TIAA.


"""





from io import TextIOWrapper
import platform
import subprocess

# ---------------------------------- Funcoes ----------------------------------
# Imprimeir a lista usando Enumarate
def print_list( list: list ):
    list_size = len(list)
    for i, item in enumerate(list):
        print( f'[ {i + 1} ]: ', item )
    print('')

def add_to_user_favorites( item ):
    favorites.append( item )
    print( f'{item} adicionado com sucesso' )

def remove_from_user_favorites( item ):
    try:
        favorites.remove( item )
        print( f'{item} removido com sucesso' )
    except ValueError:
        print('Não deveria ter conseguido chegar até essa menssagem. Esse Try é só enfeite, ta me hackeando?')

# Manipuladores de Arquivos
def protect_me( file_descriptor, file_buffer ):
    if file_buffer != '':
        if file_buffer[ 0 ] == '1':
            count: int = int( file_descriptor.readline() ) + 1
            file_descriptor.seek( 2 )
            file_descriptor.write( f'{count}\n' )
            file_descriptor.close()

                # Se tentar mais de uma, enviar mensagem
            if count >= 1:
                clear_terminal()
                print( 'Não adianta insistir baby' )
                print( f'Já tentou {count}x, não seria melhor descobrir o por quê? Será mais divertido')
        exit()

# Se executar essa função o script só executa mediante a validação de flags em um arquivo
def bye( file_name ):
    file_descriptor: TextIOWrapper = open( FILE_NAME, 'a' )
    file_descriptor.write('1\n0\n')
    file_descriptor.close()
    print( 'Te avise agora SE VIRÁ' )
    exit()


# Gerador de Menus
def init_openning_option():
    print('Escolha uma das opções e pressione ENTER para efetivar')
    print( '1 - Ver lista' )
    print( '2 - Adicionar manualmente' )
    print( '3 - Ver meus favoritos' )
    print( '4 - Quero apagar filmes dos meus favoritos' )
    print( 'OU qualquer tecla para sair')
    return input( 'opção: ')

def init_list_titles_menu():
    print( 'Lista top, não?, quer escolher algum eu deseja retornar ao menu inicial?')
    print( 'Caso queira sair, escolha 0 (zero) para retornar ao menu inicial')

def init_manual_titles_menu():
    print( 'Olha, não sou o mestre do português, mas tenta não escreve muinto errado.' )
    print( 'Se desistir só digitar 0 (zero) que devolvo para o menu incial')

def init_remove_titles_menu():
    print( 'Qual filme deseja remover?')
    print( 'Caso queira sair, já sabe 0 (zero) e vamos para o começo')


# Manipulador do terminal
def clear_terminal():
    # Referencia da NET - Danonne
    if platform.system()=="Windows":
        subprocess.Popen("cls",   shell=False).communicate() 
    else: #Linux and Mac
        subprocess.Popen("clear", shell=False).communicate() 

# ---------------------------- Final das Funcoes ------------------------------
#
#
#
# ------------------------------- INICIALICAO ---------------------------------
# limpa todo o terminal
clear_terminal()


# Inicialização das variaveis globais
movies   : list = [
    'Guerreiros da Galáxia',
    'Um Ome Morcego',
    'O Verde dos Nataiz',
    'Morbido e sua mulher abusiva', 
    'Criatividade se foi no quinto'
]
favorites: list = []



# Processo responsável por permitir ou não executar o script
# caso queira processar navemento o arquivo, basta remover o
# .byeignore ou alterar o primeiro valor para 0
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

# Primeira mensagem, não retornável
print( 'Seja bem vindo a ao NetList, seu catalogo interativo' )
print( 'Selecione os filmes listados ou, caso preferir você poderá adicionar manualmente.' )

# Fica até o usuário decidir sair
while True:
    # Inicia o primeiro menu e captura de evento do teclado
    option:str = init_openning_option()
    match option:
        case '1': # CASO QUE PERMITE O USUARIO ADICIONAR A PARTIR DE UMA LISTA
            print_list(movies)
            init_list_titles_menu()
            
            while True: 
                # Recebe um optacao supostamente numerica
                int_option: str = input('opção: ')
                
                # Verifica se o usuario quer sair, se nao vai cair na excessao
                if int_option == '0':
                    clear_terminal()
                    break

                # Caso o valor digita nao seja um numero inteiro evoca um erro
                try:
                    id = int(int_option) - 1
                    if id < len(movies):
                        add_to_user_favorites( movies[id] )
                        print_list( favorites )
                except ValueError:
                    print( 'Desculpe, mas digite apenas números inteiros.' )

        case '2': # CASO QUE PERMITE O USUARIO ADICIONAR MANUALMENTE UM TITULO
            init_manual_titles_menu()
            adicional_msg = ''
            erro_count: int = 0
            while True:
                manual_movie_title: str = input( f' {adicional_msg} --> ' )

                # Retorna ao menu inicial marotamente
                if manual_movie_title == '0':
                    clear_terminal()
                    break

                # Maquina bolada
                if manual_movie_title == '':
                    if   erro_count > 3:
                        # Setta o arquivo .byeignore com uma flag que impede o fluxo normal do script
                        bye( FILE_NAME )
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
        case '3': # CASO QUE PERMITE O USUARIO VISUALIZAR SUA LISTA DE FAVORITOS
            clear_terminal()
            print( 'Eh pra já:')
            print_list( favorites )
        case '4': # PERMITE AO USUARIO REMOVER ELEMENTOS DA LISTA
            init_remove_titles_menu()
            print_list( favorites )
            while True:
                if len(favorites) <= 0 :
                    clear_terminal()
                    print( '[[ Desculpe, não nada para remover nos seus favoritos. Tente adicionar algo antes ]]\n')
                    break
                
                # Recebe um optacao supostamente numerica
                int_option: str = input('opção: ')
                
                # Verifica se o usuario quer sair, se nao vai cair na excessao
                if int_option == '0':
                    clear_terminal()
                    break

                # Caso o valor digita nao seja um numero inteiro evoca um erro
                try:
                    id = int(int_option) - 1
                    if id < len(favorites):
                        remove_from_user_favorites( favorites[id] )
                        print_list( favorites )
                    else:
                        print( 'Olha com carinhos os números da sua lista' )
                except ValueError:
                    print( 'Desculpe, mas digite apenas números inteiros.' )
        case _: # QUALQUER TECLA PARA SAIR
            clear_terminal()
            print('Adeus, te aguardo em breve. Uma pena que esse programa ainda não tem uma persistencia de dados eficaz, vai ter qur fazer tudo de novo.')
            break


    
