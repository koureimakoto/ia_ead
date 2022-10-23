#!/usr/bin/env python3
from auth import User

"""
Como Usar:

    Primeiro importar o arquivo 'auth' para acessar a classe 'User'
    Você pode acessar de duas formas

        '
        import auth
        
        user = auth.User(NONE)
        
        '-> Essa primeira parte importa tudo que existe em Auth

        -- OU --

        '
        from auth import User

        user = User(NONE)
        
        '-> Dessa forma importará apenas a classe User


        A classe User possuí algums métodos Publicos, que são 
        funções dentro  da classe que você pode executar fora
        dela. E quase todos seus dados são ReadyOnly, que não
        permite  sobrescrever uma vez  escritos. Sendo  todos 
        dados privados Privados, isto é, para acessar estes a
        qualquer momento é  necessário invocar metódos que os 
        retornaram, claro  só os que  não comprometam a inte-
        gridade dos dados da classe.

        para 

"""




new_user = User()
new_user.create_new_user("urei@gmail.com", "#$Talles1234")
