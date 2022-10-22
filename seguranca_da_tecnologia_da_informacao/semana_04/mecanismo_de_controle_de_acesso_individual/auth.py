from   typing import Any
from   requests.exceptions import HTTPError
import pyrebase
import firebase_config
import re

class User(HTTPError):
    def __init__(self) -> None:
        super().__init__()
        self.__data      : dict = {}
        self.__email     : str  = ''
        self.__token     : str  = ''
        self.__registered: str  = ''

    # Já vi que a função tem um regex interna, mas não confio enviar requisição direto 
    # para descobrir se existe algum erro. Validação do tipo tem que ser feito antes
    # mesmo que seja por uma função interna como auth.check_user_email_and_passwd
    def create_new_user(self, email: str, passwd: str ):
        if self.__data != {}:
                return False

        if self.check_email(email) :
            try:
                firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)
                self.__set_responde(
                    firebase.auth().create_user_with_email_and_password(email, passwd)
                )
                return True
            except HTTPError as e:
                print(e)
        return False

        
        
    def get_sign_user(self, email: str, passwd: str):
        if self.check_email:
            if self.__data != {}:
                return False

            try:
                firebase = pyrebase.initialize_app(firebase_config.firebaseConfig)
                self.__set_responde(
                    firebase.auth().sign_in_with_email_and_password(email, passwd)
                )


                return True
            except HTTPError as e:
                print(e)
            return False

    def check_email(self, email: str) -> bool:
        return re.findall(r'[\w\.-]+@[\w\.-]+\.[\w]+', email) and len(email) < 256

    def __get_email(self) -> str :
        return self.__email

    def __id_token(self) -> str :
        return self.__token

    def __set_responde(self, auth) -> None:
        self.__data      = auth
        self.__email     = self.__data['email']
        self.__registered= self.__data['registered']
        self.__token     = self.__data['idToken']

    def is_registered(self) -> str :
        if self.__registered == True:
            return 'True'
        return 'False'

    def __str__(self) -> str:
        buff: str = self.__get_email() + ' '
        buff += self.is_registered()   + ' '
        return buff
